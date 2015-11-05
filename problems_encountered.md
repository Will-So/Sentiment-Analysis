# Loading the Data
1. Various JSON parsing tools (Pandas, ujson, json) fail to parise the json table
    - Cause: The files are a series of JSON objects rather than a single JSON object
    - Solution: Read the file one 'line' at a time. In this case, the line is a single json object. 
    - Other Notes: Was giving me some crazy malloc errors at first. Found that this was the case by manually looking
    at the json file and noticed that this was the case.
2. Nested vote categories (funny, helpful) when loading in the data makes the structure annoying
    - Failed Solution: After loading the Pandas Dataframe, turn it from a 'long' dataframe to a wide dataframe
        - Reason for failure: Pandas does not support this operation well. I will write a blog post implementing this in the future.
        See [here](http://stackoverflow.com/questions/22798934/pandas-long-to-wide-reshape) for a walkthrough how to do it.
    - Successful Solution: Drop the things. They are useless anyways. 