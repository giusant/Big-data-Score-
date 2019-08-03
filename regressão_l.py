from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import HashingTF, Tokenizer
from pyspark.sql import Row
from pyspark.sql.functions import UserDefinedFunction
from pyspark.sql.types import *


def csvParse(s):
    import csv
    from StringIO import StringIO
    sio = StringIO(s)
    value = csv.reader(sio).next()
    sio.close()
    return value
sc = SparkContext
inspections = sc.textFile('C:/Users/Giuliano Santiago/Google Drive/cs-training.csv').map(csvParse)

schema = StructType([
StructField("ID", IntegerType(), False),
StructField("age", IntegerType(), False),
StructField("NumberOfTime30-59DaysPastDueNotWorse", IntegerType(), False),
StructField("MonthlyIncome", IntegerType(), False),
StructField("NumberOfOpenCreditLinesAndLoans", IntegerType(), False),
StructField("NumberOfTimes90DaysLate", IntegerType(), False),
StructField("NumberRealEstateLoansOrLines", IntegerType(), False),
StructField("NumberOfTime60-89DaysPastDueNotWorse", IntegerType(), False),
StructField("NumberOfDependents", IntegerType(), False),
StructField("SeriousDlqin2yrs", IntegerType(), False),
StructField("Class",StringType, False)])

df = spark.createDataFrame(inspections.map(lambda l: (int(l[0]), l[1], l[2],l[3],l[4],l[5],l[6],l[7],
l[8],l[9],l[10],l[11],) , schema))
df.registerTempTable('CountResults')

df.show(5)

