from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import BinaryClassificationEvaluator

def train_model():
    spark = SparkSession.builder.appName("Sentiment140Model").getOrCreate()
    df = spark.read.csv("data/cleaned_data.csv", header=True, inferSchema=True)
    df = df.withColumnRenamed("sentiment", "label")

    tokenizer = Tokenizer(inputCol="clean_text", outputCol="words")
    remover = StopWordsRemover(inputCol="words", outputCol="filtered")
    hashingTF = HashingTF(inputCol="filtered", outputCol="rawFeatures", numFeatures=10000)
    idf = IDF(inputCol="rawFeatures", outputCol="features")
    lr = LogisticRegression(maxIter=10)

    pipeline = Pipeline(stages=[tokenizer, remover, hashingTF, idf, lr])
    (trainingData, testData) = df.randomSplit([0.8, 0.2])
    model = pipeline.fit(trainingData)
    predictions = model.transform(testData)

    evaluator = BinaryClassificationEvaluator()
    print("Accuracy:", evaluator.evaluate(predictions))
