from itertools import chain,cycle
import math


def plot_nulls(*dataframes, columns=2, titles=cycle(['']), width=5, height=4.5):
    """
    This function gets dataframes or numpy arrays and returns a plot that
    represents the null values in it.
          Args:
              dataframes (a dataframe or numpy array)
              columns (int): The number of columns in the subplots.
              titles (a list of strings): The titles of the plots.
              width (int): Width of the plot images.
              height (int): Height of the plot images.

          Returns:
              Plots: Returns nothing but plots the result.
  """
    def isNpArray(array):
        return isinstance(array, type( np.array([])) )
    ##
    def get_nulls(df, notnull=False):
        # Extract the null or not-null count from dataframes
        elements = []
        if not isNpArray(df):
            if notnull == True:
                elements.extend([ df[column].notna().sum() for column in df ])
            else:
                elements.extend([ df[column].isna().sum() for column in df])
        else:
            if notnull == True:
                elements.append(len(df)-np.isnan(df).sum())
            else:
                elements.append(np.isnan(df).sum())
        return elements # Such as the list [35,53,12,52] holding the null
                            # counts of all the columns.
    ##
    def get_row(count):
        # Round the half of the count to the upper number.
        return math.ceil(count/columns) # Like 5/2 = 3
    ##
    df_count = len(dataframes)
    total_row = get_row(df_count)
#     print('totalrow=',total_row, 'df_count=',df_count)
    fig, axs = plt.subplots(total_row, columns,figsize=(width*columns,
                                                        height*total_row),
                                                        dpi=100)
    ##
    for count, df in enumerate(dataframes,1):
        if total_row == 1 or columns==1:
            bar = axs[count-1]
        else:
            row = get_row(count)-1
            column = (count-1)%columns
            bar = axs[row,column]
        ##
        if isNpArray(df):
            columns = 0
        else:
            columns = df.columns
        ##
        bar.barh(y= columns,
                 width=get_nulls(df),
                 label='Null Elements',
                 color= 'tab:red')
        bar.barh(y= columns,
                 width=get_nulls(df,notnull=True),
                 left=get_nulls(df),
                 label='Not-Null Elements',
                 color='steelblue')
        bar.set_title(str(count))
        bar.invert_yaxis()
        bar.legend()

    fig.tight_layout()
    fig.show()
