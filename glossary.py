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
An optimisation in Spark where several map operations are combined into a single step.
"""

definition = """
WholeStageCodeGen is an optimisation in Spark where several map operations are combined into a single step of the code that Spark generates.  You can think of this as two lambda funnctions (steps) being combined into a single lambda function for execution.
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
Actions are RDD operations that produce non-RDD values. They materialize a value in a Spark program.  See [here](https://jaceklaskowski.gitbooks.io/mastering-apache-spark/spark-rdd-actions.html).

See also [here](https://medium.com/@aristo_alex/how-apache-sparks-transformations-and-action-works-ceb0d03b00d0)
"""

add_to_glossary("action", short_definition, definition)

with open("glossary.json", "w") as f:
  json.dump(glossary, f, indent=4)
