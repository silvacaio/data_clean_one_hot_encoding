class clean_data:
    def __init__(self, df):
        self.data = df

    def one_hot_encoding_column(self, column_name, remove_original_column):

        #get unique values
        columns = self.data[column_name].unique()

        # add new columns for each value
        for column in columns:
            self.data[column] = 0 #default value

        for index, row in self.data.iterrows():
            for column in columns:
                if column == row[column_name]:
                    self.data.at[index, column] = 1
                    break

        if remove_original_column:
            del self.data[column_name]

