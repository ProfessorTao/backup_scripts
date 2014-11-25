package test.map_reduce;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.ArrayWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// Hadoop觉得Java的序列化不适合自己，于是实现了IntWritable类
// Mapper类很重要，它将输入键值对映射到输出键值对，也就是MapReduce里的Map过程。

public class TokenizerMapper extends Mapper<Object, Text, Text, IntWritable>{
	// 自己的Map过程，类名是TokenizerMapper，它继承了Hadoop的Mapper类
	// 1. Object: 输入键key的参数类型
	// 2. Text: 表示输入值的类型
	// 3. Text: 表示输出键类型
	// 4. IntWriable: 表示输出键类型	

    IntWritable one = new IntWritable(1); // 定义输出值，初始始终是1
    Text word = new Text(); // 定义输出键
    
    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
    	// 定义map函数，函数有三个参数，key是输入键，它是什么无所谓，实际上用不到它的，value是输入值。
    	// 在map函数中，出错的时候会抛出异常，所以有“throwsIOException, InterruptedException”。
    	// Context类的定义是在TokenizerMapper的祖先类Mapper的内部，不需要引入，如果去查看Mapper类的源代码的话，能看到Context类是继承MapContext类的。
    	
    	char[] c_list = {1, 2, 3, '\n'};
    	String delim = "";
        for (char c: c_list) {
            delim += String.valueOf(c);
        }
        
        StringTokenizer itr = new StringTokenizer(value.toString(), delim);
        // 定义StringTokenizer对象itr，StringTokenizer的构造函数只接受Java的String类，而value是Text类，所以要进行转化，将value转成String类，也就是“value.toString()”。
                
        while(itr.hasMoreTokens()) {
        	// 在默认的情况下，StringTokenizer以空格符作为分隔符对字符串进行解析，每次解析会先调用hasMoreTokens看看是不是需要做解析，如果需要做，就用nextToken()函数获取解析结果，然后用这个结果给word赋值，然后，再将word和one作为一个键值对写到context里，context会存储键值留待Reduce过程处理。
        	
            word.set(itr.nextToken());
            context.write(word,one);
        }
    } // end of map
} // end of class

