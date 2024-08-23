cat test.txt | python3 mapper.py

cat으로 불러온 파일 읽어서 파이썬 실행

cat test.txt | python3 mapper.py | sort

sort (shuffling)하둡이 해주는 작업



error
WARNING: Attempting to start all Apache Hadoop daemons as ubuntu in 10 seconds.
WARNING: This is not a recommended production deployment configuration.
WARNING: Use CTRL-C to abort.
Starting namenodes on [localhost]
localhost: namenode is running as process 6447.  Stop it first and ensure /tmp/hadoop-ubuntu-namenode.pid file is empty before retry.
Starting datanodes
localhost: datanode is running as process 6596.  Stop it first and ensure /tmp/hadoop-ubuntu-datanode.pid file is empty before retry.
Starting secondary namenodes [2-12]
2-12: secondarynamenode is running as process 6782.  Stop it first and ensure /tmp/hadoop-ubuntu-secondarynamenode.pid file is empty before retry.
Starting resourcemanager
resourcemanager is running as process 6986.  Stop it first and ensure /tmp/hadoop-ubuntu-resourcemanager.pid file is empty before retry.
Starting nodemanagers
localhost: nodemanager is running as process 7111.  Stop it first and ensure /tmp/hadoop-ubuntu-nodemanager.pid file is empty before retry.

어제 수업하고 실행정지 안했더니 에러 발생.. 
sbin/stop-all.sh 명령어 입력하고 실행중지 시켜주고 다시 실행하면 정상작동



requestly 경로변환하려고 사용
2.12. -> localhost



hadoop으로 MapReduce job 실행 
hadoop jar $HADOOP_HOME/share/hadoop/tools

 hadoop jar ~/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \   
-input /user/ubuntu/input/test.txt \    
-output /user/ubuntu/output/wordcount \    
-mapper 'python3 /home/ubuntu/dmf/0.wordcount/mapper.py'   
-reducer 'python3 /home/ubuntu/dmf/0.wordcount/reducer/py'   


output (결과저장할 경로)   
input (시작해야할 파일경로)   
input,output은 하둡의 경로   
mapper,reducer 파이썬 실행하는 경로(리눅스)   

폴더를 지우는 명령어
hdfs dfs -rm -r 


hadoop jar ~/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-input /user/ubuntu/input/u.data \
-output /user/ubuntu/output/movie-avg \
-mapper 'python3 /home/ubuntu/dmf/1.movie-rate-avg/mapper.py' \
-reducer 'python3 /home/ubuntu/dmf/1.movie-rate-avg/reducer/py' 

hadoop jar ~/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-input /user/ubuntu/input/u.data \
-output /user/ubuntu/output/movie-avg \
-mapper 'python3 /home/ubuntu/dmf/hadoop/1.movie-rate-avg/mapper.py' \
-reducer 'python3 /home/ubuntu/dmf/hadoop/1.movie-rate-avg/reducer.py'


hadoop 앞에 뛰어쓰기로 인한 오류.... 
항상 오타 조심 

packageJobJar: [/tmp/hadoop-unjar6145638276534899313/] [] /tmp/streamjob5980810735757930261.jar tmpDir=null
2024-08-23 14:37:03,649 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
2024-08-23 14:37:03,839 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
2024-08-23 14:37:04,040 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/ubuntu/.staging/job_1724378859099_0002
2024-08-23 14:37:04,250 INFO mapred.FileInputFormat: Total input files to process : 1
2024-08-23 14:37:04,304 INFO mapreduce.JobSubmitter: number of splits:2
2024-08-23 14:37:04,848 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1724378859099_0002
2024-08-23 14:37:04,848 INFO mapreduce.JobSubmitter: Executing with tokens: []
2024-08-23 14:37:04,984 INFO conf.Configuration: resource-types.xml not found
2024-08-23 14:37:04,984 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2024-08-23 14:37:05,036 INFO impl.YarnClientImpl: Submitted application application_1724378859099_0002
2024-08-23 14:37:05,065 INFO mapreduce.Job: The url to track the job: http://2-12.:8088/proxy/application_1724378859099_0002/
2024-08-23 14:37:05,067 INFO mapreduce.Job: Running job: job_1724378859099_0002
2024-08-23 14:37:10,127 INFO mapreduce.Job: Job job_1724378859099_0002 running in uber mode : false
2024-08-23 14:37:10,129 INFO mapreduce.Job:  map 0% reduce 0%
2024-08-23 14:37:13,180 INFO mapreduce.Job: Task Id : attempt_1724378859099_0002_m_000001_0, Status 
: FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 2
        at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:326)
        at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:539)
        at org.apache.hadoop.streaming.PipeMapper.close(PipeMapper.java:130)
        at org.apache.hadoop.mapred.MapRunner.run(MapRunner.java:61)
        at org.apache.hadoop.streaming.PipeMapRunner.run(PipeMapRunner.java:34)
        at org.apache.hadoop.mapred.MapTask.runOldMapper(MapTask.java:466)
        at org.apache.hadoop.mapred.MapTask.run(MapTask.java:350)
        at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:178)
        at java.security.AccessController.doPrivileged(Native Method)
        at javax.security.auth.Subject.doAs(Subject.java:422)
        at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1899)     
        at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:172)

2024-08-23 14:37:13,191 INFO mapreduce.Job: Task Id : attempt_1724378859099_0002_m_000000_0, Status 
: FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 2    
        at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:326)
        at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:539)
        at org.apache.hadoop.streaming.PipeMapper.close(PipeMapper.java:130)
        at org.apache.hadoop.mapred.MapRunner.run(MapRunner.java:61)
        at org.apache.hadoop.streaming.PipeMapRunner.run(PipeMapRunner.java:34)
        at org.apache.hadoop.mapred.MapTask.runOldMapper(MapTask.java:466)
        at org.apache.hadoop.mapred.MapTask.run(MapTask.java:350)
        at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:178)
        at java.security.AccessController.doPrivileged(Native Method)
        at javax.security.auth.Subject.doAs(Subject.java:422)
        at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1899)     
        at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:172)

2024-08-23 14:37:17,223 INFO mapreduce.Job: Task Id : attempt_1724378859099_0002_m_000001_1, Status 
: FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 2
        at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:326)
        at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:539)
        at org.apache.hadoop.streaming.PipeMapper.close(PipeMapper.java:130)
        at org.apache.hadoop.mapred.MapRunner.run(MapRunner.java:61)
        at org.apache.hadoop.streaming.PipeMapRunner.run(PipeMapRunner.java:34)
        at org.apache.hadoop.mapred.MapTask.runOldMapper(MapTask.java:466)
        at org.apache.hadoop.mapred.MapTask.run(MapTask.java:350)
        at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:178)
        at java.security.AccessController.doPrivileged(Native Method)
        at javax.security.auth.Subject.doAs(Subject.java:422)
        at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1899)     
        at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:172)

2024-08-23 14:37:18,231 INFO mapreduce.Job: Task Id : attempt_1724378859099_0002_m_000000_1, Status 
: FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 2
        at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:326)
        at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:539)
        at org.apache.hadoop.streaming.PipeMapper.close(PipeMapper.java:130)
        at org.apache.hadoop.mapred.MapRunner.run(MapRunner.java:61)
        at org.apache.hadoop.streaming.PipeMapRunner.run(PipeMapRunner.java:34)
        at org.apache.hadoop.mapred.MapTask.runOldMapper(MapTask.java:466)
        at org.apache.hadoop.mapred.MapTask.run(MapTask.java:350)
        at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:178)
        at java.security.AccessController.doPrivileged(Native Method)
        at javax.security.auth.Subject.doAs(Subject.java:422)
        at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1899)     
        at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:172)

2024-08-23 14:37:19,238 INFO mapreduce.Job: Task Id : attempt_1724378859099_0002_m_000001_2, Status 
: FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 2
        at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:326)
        at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:539)
        at org.apache.hadoop.streaming.PipeMapper.close(PipeMapper.java:130)
        at org.apache.hadoop.mapred.MapRunner.run(MapRunner.java:61)
        at org.apache.hadoop.streaming.PipeMapRunner.run(PipeMapRunner.java:34)
        at org.apache.hadoop.mapred.MapTask.runOldMapper(MapTask.java:466)
        at org.apache.hadoop.mapred.MapTask.run(MapTask.java:350)
        at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:178)
        at java.security.AccessController.doPrivileged(Native Method)
        at javax.security.auth.Subject.doAs(Subject.java:422)
        at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1899)     
        at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:172)

2024-08-23 14:37:21,251 INFO mapreduce.Job: Task Id : attempt_1724378859099_0002_m_000000_2, Status 
: FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 2
        at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:326)
        at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:539)
        at org.apache.hadoop.streaming.PipeMapper.close(PipeMapper.java:130)
        at org.apache.hadoop.mapred.MapRunner.run(MapRunner.java:61)
        at org.apache.hadoop.streaming.PipeMapRunner.run(PipeMapRunner.java:34)
        at org.apache.hadoop.mapred.MapTask.runOldMapper(MapTask.java:466)
        at org.apache.hadoop.mapred.MapTask.run(MapTask.java:350)
        at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:178)
        at java.security.AccessController.doPrivileged(Native Method)
        at javax.security.auth.Subject.doAs(Subject.java:422)
        at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1899)     
        at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:172)

2024-08-23 14:37:23,265 INFO mapreduce.Job:  map 100% reduce 100%
2024-08-23 14:37:23,280 INFO mapreduce.Job: Job job_1724378859099_0002 failed with state FAILED due 
to: Task failed task_1724378859099_0002_m_000001
Job failed as tasks failed. failedMaps:1 failedReduces:0 killedMaps:0 killedReduces: 0

2024-08-23 14:37:23,332 INFO mapreduce.Job: Counters: 14
        Job Counters
                Failed map tasks=7
                Killed map tasks=1
                Killed reduce tasks=1
                Launched map tasks=8
                Other local map tasks=6
                Data-local map tasks=2
                Total time spent by all maps in occupied slots (ms)=12877
                Total time spent by all reduces in occupied slots (ms)=0
                Total time spent by all map tasks (ms)=12877
                Total vcore-milliseconds taken by all map tasks=12877
                Total megabyte-milliseconds taken by all map tasks=13186048
        Map-Reduce Framework
                CPU time spent (ms)=0
                Physical memory (bytes) snapshot=0
                Virtual memory (bytes) snapshot=0
2024-08-23 14:37:23,332 ERROR streaming.StreamJob: Job not successful!
Streaming Command Failed!



정규표현식 - 찾고자 하는 문자열 형태지정
\d : digit 숫자
\d{2} : 2자리 숫자
:(\d{2}):(\d{2}):(\d{2})
