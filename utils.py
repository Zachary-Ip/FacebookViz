import os
import json
import pandas as pd


def LoadMessages(directory):
    """
    Import facebook data from a json file

    Args:
        directory (str): path to folder containing messages

    Return:
        df (DataFrame): dataframe
    """
    os.chdir(directory)
    files = os.listdir()

    messages = [match for match in files if "message" in match]
    all_messages = []
    for i in messages:
        f = open(i)
        full_data = json.load(f)
        messages = full_data["messages"]
        all_messages = all_messages + messages

    df = pd.DataFrame(all_messages)
    return df


def CleanData(df):
    """
    Remove unused columns from dataframe.

    Args (Dataframe): Dataframe of chat data

    """
    # Add new columns to dataframe
    df.index = pd.to_datetime(df["timestamp_ms"], unit="ms")

    df["day"] = df.index.dayofweek
    df["date"] = df.index.date
    df["time"] = df.index.hour

    # Remove unused dataframes
    df_clean = df.drop(
        columns=[
            "is_unsent",
            "call_duration",
            "share",
            "photos",
            "videos",
            "files",
            "audio_files",
            "gifs",
            "missed",
            "reactions",
        ]
    )
    return df_clean
