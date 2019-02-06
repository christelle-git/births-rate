from IPython.display import display, HTML 
import pandas as pd
import numpy as np
import datetime

def remove_nan_entries(df):
	"""
            Remove the NaN values of the Dataset.

	    * Args: df (pandas.DataFrame)
            * Return: clean_df (pandas.DataFrame) 

	"""
	df_initsize = len(df)
	print('Initial dataset size: ', df.shape)
	display(HTML(df.tail().to_html()))
	print('\nRemoving the NaN values...')
	
	for col in df.columns:
	    col_type = df[col].dtype
	    #print('col infos: {} dtype={}'.format(col, col_type))
	    if(col_type != np.dtype('int64')):	df.drop(df[~df[col].notna()].index, inplace=True)

	display(HTML(df.tail().to_html()))
	print('\nDataset size after NaN removing: ', df.shape)
	red_per = 100*(df_initsize - len(df)) / df_initsize
	print("=> %.0f%% reduction of data." % red_per)

	return df


def remove_outliers_date(df):
	"""
            Remove the values of days > 31 and the years > 1989.

	    * Args: df (pandas.DataFrame)
            * Return: clean_df (pandas.DataFrame) 

	"""
	df_initsize = len(df)
	print('Initial dataset size: ', df.shape)
	display(HTML(df[df['day'] > 31].head().to_html()))
	print('Removing the 99 days...')
	df.drop(df[df['day'] > 31].index, inplace=True)
	print('Dataset size after cleaning: ', df.shape)
	red_per = 100*(df_initsize - len(df)) / df_initsize
	print("=> %.0f%% reduction of data." % red_per)

	df_size = len(df)
	print('\nRemoving years > 1989...')
	df.drop(df[df['year'] > 1989].index, inplace=True) 

	print('Dataset size after cleaning: ', df.shape)
	red_per = 100*(df_size - len(df)) / df_size
	print("=> %.0f%% reduction of data." % red_per)
        
	return df


def date_conversion(df):
	"""
            Convert the date into datetime format.
	    Add the name of the day.
	    Clean the NaT.

	    * Args: df (pandas.DataFrame)
            * Return: clean_df (pandas.DataFrame) 

	"""
	print('Initial dataset size: ', df.shape)
	display(HTML(df.head().to_html()))

	print('Date conversion...')
	# to_datetime conversion
	data_dt = pd.to_datetime(df[['year','month','day']], 
				format='%Y%m%d', errors="coerce")
	# day of the week conversion
	data_dow = data_dt.dt.dayofweek

	# conversion into DataFrame
	data_df = pd.DataFrame({'date':data_dt,
                        'weekday':data_dow.values, 
                        'births':df['births']})
	# column with the name of the day
	data_df["dayname"] = data_df["date"].dt.day_name()  

	# Remove DateTime outliers NaT
	print('Removing NaT...')
	#display(HTML(data_df[~data_df.date.notnull()].head().to_html()))
	df = data_df[data_df.date.notnull()]
	display(HTML(df.head().to_html()))

	print('Final dataset size {}'.format(df.shape))
	
	return df


def get_grouped_mean(df, df_groupby):
	"""
     	    Group data by the day of the week.
	    Average births for each weekday.

	    * Args: df (pandas.DataFrame)
            * Return: clean_df (pandas.DataFrame) 

	"""
	print('Grouped by weekday.')
	df_gb = df.groupby(df_groupby)
	print('Averaging the number of births for each day of the week...')
	df_mean = df_gb['births'].mean()
	print(df_mean)

	return df_mean
 	


















