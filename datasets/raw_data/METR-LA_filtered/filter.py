import pandas as pd

def load_and_process_data(file_path):
    # Load the data
    df = pd.read_hdf(file_path)

    # Convert index to datetime
    df.index = pd.to_datetime(df.index)

    # Try removing the frequency attribute if it exists
    if hasattr(df.index, 'freq'):
        df.index.freq = None

    # Print basic details about the index
    print("Index type:", type(df.index))
    print("First few index entries:", df.index[:5])



    return df

if __name__ == "__main__":
    file_path = "metr-la.h5"
    df = load_and_process_data(file_path)

    # Specify date range for filtering
    start_date = '2012-03-01'
    end_date = '2012-03-31'

    # Filter the data
    filtered_df = df.loc[start_date:end_date]

    # Print the filtered data
    print(filtered_df)
    # Optionally save the filtered data
    df.to_hdf("metr-la-filtered.h5", key="df", mode="w")
