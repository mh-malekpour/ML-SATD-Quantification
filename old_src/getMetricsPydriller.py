from pydriller import Repository
import pandas as pd

df = pd.read_csv('filtered_data_second_half.csv')
df_cleaned = df.dropna(subset=['ML TD Type'])
filtered_df = df_cleaned[(df_cleaned['Comment-Removing Revision'] != "STILL_EXISTS") & (df_cleaned['ML TD Type'] != "nan")]

for index, row in filtered_df.iterrows():
    start_commit = row['Comment-Introducing Revision'].split('/')[-1]
    end_commit = row['Comment-Removing Revision'].split('/')[-1]
    count_commits = 1
    print('Start commit: {}, End commit: {}'.format(start_commit, end_commit))

    for commit in Repository('https://github.com/' + row['Repo Name'], from_commit=start_commit, to_commit=end_commit).traverse_commits():
        print('Commit: {}'.format(commit.hash))
        count_commits += 1
        if commit.hash == start_commit or commit.hash == end_commit:
            for m in commit.modified_files:
                if m.filename == row['Filename'].split('/')[-1]:
                    # print(
                    #     'The commit {} has been modified in date {}'.format(
                    #         commit.hash,
                    #         commit.committer_date
                    #     )
                    # )
                    # print('lines of code: {}, complexity: {}'.format(m.nloc, m.complexity))


                    if commit.hash == start_commit:
                        filtered_df.loc[index, 'Change Type Start'] = m.change_type
                        filtered_df.loc[index, 'Lines of Code Start'] = m.nloc
                        filtered_df.loc[index, 'Complexity Start'] = m.complexity
                        filtered_df.loc[index, 'Added Lines Start'] = m.added_lines
                        filtered_df.loc[index, 'Deleted Lines Start'] = m.deleted_lines
                        filtered_df.loc[index, 'Changed Methods Start'] = len(m.changed_methods)
                        filtered_df.loc[index, 'Token Count Start'] = m.token_count
                    if commit.hash == end_commit:
                        filtered_df.loc[index, 'Change Type End'] = m.change_type
                        filtered_df.loc[index, 'Lines of Code End'] = m.nloc
                        filtered_df.loc[index, 'Complexity End'] = m.complexity
                        filtered_df.loc[index, 'Added Lines End'] = m.added_lines
                        filtered_df.loc[index, 'Deleted Lines End'] = m.deleted_lines
                        filtered_df.loc[index, 'Changed Methods End'] = len(m.changed_methods)
                        filtered_df.loc[index, 'Token Count End'] = m.token_count
                        filtered_df.loc[index, 'Commits Between Start End'] = count_commits

filtered_df.to_csv('data_with_metrics.csv', index=False)