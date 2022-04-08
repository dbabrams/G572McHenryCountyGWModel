{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "117e0e47-728d-4948-807b-eafe47e9843e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "from simpledbf import Dbf5\n",
    "import numpy as np\n",
    "\n",
    "# read in dbf to pandas dataframe\n",
    "file = 'C:/users/andrewm4/Documents/Hydro_572/GitHub/G572McHenryCountyGWModel/GISuploads/hydraulic_conductivity.dbf'\n",
    "dbf = Dbf5(file)\n",
    "df = dbf.to_dataframe()\n",
    "df.head()\n",
    "\n",
    "# create dataframes of the 10 zones, Kx, Ky, and Kz\n",
    "zone = df[df.columns[pd.Series(df.columns).str.contains(\"Z\")]]\n",
    "x = df[df.columns[pd.Series(df.columns).str.contains(\"x\")]]\n",
    "y = df[df.columns[pd.Series(df.columns).str.contains(\"y\")]]\n",
    "z = df[df.columns[pd.Series(df.columns).str.contains(\"z\")]]\n",
    "\n",
    "# define the function that converts data frame to array; reshapes it and saves as variable\n",
    "# 3D array of 10 layers by 205 rows by 225 columns\n",
    "def array_shaper(j):\n",
    "    j = j.to_numpy()\n",
    "    j = np.reshape(j, (205,225,10)) # 205 = y; 225 = x\n",
    "    return j\n",
    "\n",
    "# save function output to variables\n",
    "zone_reshaped = array_shaper(zone)\n",
    "x_reshaped = array_shaper(x)\n",
    "y_reshaped = array_shaper(y)\n",
    "z_reshaped = array_shaper(z)\n",
    "\n",
    "# check shape\n",
    "print(zone_reshaped.shape)\n",
    "print(x_reshaped.shape)\n",
    "print(y_reshaped.shape)\n",
    "print(z_reshaped.shape)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
