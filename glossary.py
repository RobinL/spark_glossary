import json

glossary = {}

def add_to_glossary(key, short_definition, definition):
  glossary[key] = {
    "short_definition": short_definition.strip(),
    "definition": definition.strip(),
    "key": key
  }

# Exchange
short_definition = """
An exchange is shorthand for a 'shuffle exchange', often described merely as a 'shuffle'.
"""

definition = """
'Exchange' is shorthand for a 'Shuffle Exchange. This means that Spark is sending intermediate data between executors, probably across the network. This is more often described as merely a 'shuffle'.  This happens between jobs.
"""

add_to_glossary("exchange", short_definition, definition)

# Project
short_definition = """
Picking a subset of available columns
"""

definition = """
This 'can be roughly thought of as picking a subset of all available columns. For example, if the attributes are (name, age), then projection of the relation {(Alice, 5), (Bob, 8)} onto attribute list (age) yields {5,8}"
"""

add_to_glossary("project", short_definition, definition)

# Shuffle
short_definition = """
A procedure for spark executors either in same physical node or in different physical nodes to exchange intermedia data generated by map tasks and required by reduce tasks.
"""

definition = """
Certain operations within Spark trigger an event known as the shuffle. The shuffle is Spark’s mechanism for re-distributing data so that it’s grouped differently across partitions. This typically involves copying data across executors and machines, making the shuffle a complex and costly operation.  See [here](https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations)

A procedure for spark executors either in same physical node or in different physical nodes to exchange intermedia data generated by map tasks and required by reduce tasks.  See [here]
(https://xuechendi.github.io/2019/04/15/Spark-Shuffle-and-Spill-Explained)

"""

add_to_glossary("shuffle", short_definition, definition)


# Stage
short_definition = "Jobs are divided into 'stages' based on the shuffle boundary"

definition = """
Jobs are divided into "stages" based on the shuffle boundary.
A stage is a collection of tasks that run the same code, each on a different subset of the data. See [here](https://stackoverflow.com/a/42266758/1779128) and [here](https://docs.cloudera.com/documentation/enterprise/5-6-x/topics/cdh_ig_spark_apps.html).
"""

add_to_glossary("stage", short_definition, definition)

# Job
short_definition = """
A job is created when you apply an action on an RDD.  There is a one to one correspondence between actions and jobs.
"""

definition = """
A job is created when you apply an action on an RDD.    See [here](https://intellipaat.com/community/18528/what-is-the-concept-of-application-job-stage-and-task-in-spark) and [here](https://www.waitingforcode.com/apache-spark/jobs-stages-tasks/read).
"""

add_to_glossary("job", short_definition, definition)

# WholeStageCodeGen

short_definition = """
An optimisation in Spark where several operations are 'fused' (combined) into a single operation.
"""

definition = """
WholeStageCodeGen is an optimisation in Spark where several map operations are combined into a single step of the code that Spark generates.  You can think of this as two or more lambda funnctions (steps) being combined into a single lambda function for execution.

Spark SQL engine not only generates codes for the expressions in the physical operator tree but also generates code for the entire tree along with the expressions.  See [here](https://youtu.be/ywPuZ_WrHT0?t=654).

The generated code elimited virtual function calls, thus enabling a lot more optimisation opportuities for the java compiling.
"""

add_to_glossary("wholestagecodegen", short_definition, definition)

# Task

short_definition = """
Each stage in a job is divided into tasks based on the number of partitions in an RDD.  Every task in a stage does the same thing on a different segment of the data.
"""

definition = """
Each stage is further divided into tasks based on the number of partitions in the RDD. So tasks are the smallest units of work for Spark.
Every task inside a stage does the exact same thing, only on a different segment of the data. If a task is required to do something different, it's required that it be part of another stage.
Tasks which are running the same code on different subsets (partitions) of the data can be collected into stages.
One task is operated on by one core which is one partition.  See [here](https://stackoverflow.com/questions/42263270/what-is-the-concept-of-application-job-stage-and-task-in-spark)
"""

add_to_glossary("task", short_definition, definition)

# Collect

short_definition = """
Return all the elements of the dataset as an array at the driver program.
"""

definition = """
Return all the elements of the dataset as an array at the driver program. This is usually useful after a filter or other operation that returns a sufficiently small subset of the data. See [here](https://spark.apache.org/docs/latest/rdd-programming-guide.html).
"""

add_to_glossary("collect", short_definition, definition)

# HashPartitioning

short_definition = """
A type of shuffle where data is allocated to partitions (executors) based on the modulus of the hash of a value.  The value chosen will ensure data that needs to be processed together is sent to the same partition.
"""

definition = """
A type of shuffle where data is allocated to partitions (executors) based on the modulus of the hash of a value.  The value chosen will ensure data that needs to be processed together is sent to the same partition.  For instance, in the case of a join, the value which is hashed will be the join key.
"""

add_to_glossary("hashpartitioning", short_definition, definition)

with open("glossary.json", "w") as f:
  json.dump(glossary, f, indent=4)


# Action

short_definition = """
Actions return final results of RDD computations, e.g. writing out data to the filesystem, or showing a dataframe in a REPL.  Due to lazy evaluation, actions 'trigger' computations to occur in Spark.
"""

definition = """
An action tell Spark to yield a result from a series of transformations.  There are three types of action:

- View data in repl/console
- Collect data to native objects in e.g. Python
- Write out data

Actions are RDD operations that produce non-RDD values. They materialize a value in a Spark program.  See [here](https://jaceklaskowski.gitbooks.io/mastering-apache-spark/spark-rdd-actions.html).

See also [here](https://medium.com/@aristo_alex/how-apache-sparks-transformations-and-action-works-ceb0d03b00d0)
"""

add_to_glossary("action", short_definition, definition)


# RoundRobinPartitioning

short_definition = """
Distributes elements evenly across output partitions, starting from a random partition.  Row 1 goes to a random partition, row 2 goes to the next partition etc.
"""

definition = """
Distributes elements evenly across output partitions, starting from a random partition.  Row 1 goes to a random partition, row 2 goes to the next partition etc.  See [here](https://github.com/apache/spark/blob/7f2c88d66392340212cd79cda6464ee20263dc43/sql/core/src/main/scala/org/apache/spark/sql/execution/exchange/ShuffleExchangeExec.scala#L238)
"""
add_to_glossary("roundrobinpartitioning", short_definition, definition)

# HashAggregate

short_definition = """
Reduces data based on the modolus of the hash of zero or more keys.
"""

definition = """
Reduces data based on the modolus of the hash of zero or more keys.
"""

add_to_glossary("hashaggregate", short_definition, definition)

# Predicate

short_definition  = "A predicate is a condition on a query that returns true or false, typically located in the WHERE clause. "

definition = "A predicate is a condition on a query that returns true or false, typically located in the WHERE clause. Predicate pushdown is where Spark pushes these filters to the data read operation (from a database or files), reducing the number of entries retrieved from the data source and improving query performance."

add_to_glossary("predicate", short_definition, definition)

# RangePartitioning

short_definition = "A partitioning strategy that assigns data to partitions based on an ordering.  Each partition will have a min and a max row, relative to the given ordering.  All rows that are in between this min and max will reside in this partition"

definition = """Represents a partitioning where rows are split across partitions based on some total ordering of
the expressions specified in `ordering`.  When data is partitioned in this manner the following two conditions are guaranteed to hold:
 - All row where the expressions in `ordering` evaluate to the same values will be in the same
   partition.
 - Each partition will have a `min` and `max` row, relative to the given ordering.  All rows
   that are in between `min` and `max` in this `ordering` will reside in this partition.

See [here](https://github.com/apache/spark/blob/0a4c03f7d084f1d2aa48673b99f3b9496893ce8d/sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/plans/physical/partitioning.scala#L243)
"""

add_to_glossary("rangepartitioning", short_definition, definition)
with open("glossary.json", "w") as f:
  json.dump(glossary, f, indent=4)



with open("glossary.json", "w") as f:
  json.dump(glossary, f, indent=4)
