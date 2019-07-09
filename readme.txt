方法一：
echo $CLASSPATH

export $CLASSPATH=".:/root/sqlite-jdbc-3.27.2.1.jar"

java Read


方法二：
java -classpath ".:/root/sqlite-jdbc-3.27.2.1.jar" Read


从那个地方找到第三方包，缺省从CLASSPATH路径中找
