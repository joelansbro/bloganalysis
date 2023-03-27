import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.DataFrame

def readability(df):
  # Compute the Flesch reading ease score for each article.
  df["flesch_reading_ease"] = df["words"].toDouble() / df["sentences"].toDouble()

  # Compute the Gunning fog index for each article.
  df["gunning_fog_index"] = 2 * df["words"].toDouble() / df["sentences"].toDouble() + 12

  # Rank the articles by their readability score.
  df.sortBy(df["flesch_reading_ease"], ascending=False).show()

def main(args):
  # Create a SparkSession.
  spark = SparkSession.builder().master("local").appName("readability").build()

  # Create a DataFrame of words.
  words = spark.createDataFrame(
    [
      "The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"
    ]
  )

  # Compute the Flesch reading ease score for each article.
  words.withColumn("sentences", words.words.split(" ").count()).withColumn("flesch_reading_ease", words.words.toDouble() / words.sentences.toDouble())

  # Compute the Gunning fog index for each article.
  words.withColumn("gunning_fog_index", 2 * words.words.toDouble() / words.sentences.toDouble() + 12)

  # Rank the articles by their readability score.
  words.sortBy(words["flesch_reading_ease"], ascending=False).show()

if __name__ == "__main__":
  main(args)