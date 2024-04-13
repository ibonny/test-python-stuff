import pandas as pd
import numpy as np
from klepto.archives import dict_archive, file_archive

def main():
    print("stuff")

    m = [1, 2, 3, 4, 5]

    df = pd.DataFrame(m)

    print(df)

    fa = file_archive("testout.dict")

    fa["df"] = df


if __name__ == "__main__":
    main()