package test.map_reduce;

import java.io.IOException;
//import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.ArrayWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// Hadoop觉得Java的序列化不适合自己，于是实现了IntWritable类
// Mapper类很重要，它将输入键值对映射到输出键值对，也就是MapReduce里的Map过程。

public class TokenizerMapper extends Mapper<Object, Text, Text, IntArrayWritable>{
	// 自己的Map过程，类名是TokenizerMapper，它继承了Hadoop的Mapper类
	// 1. Object: 输入键key的参数类型
	// 2. Text: 表示输入值的类型
	// 3. Text: 表示输出键类型
	// 4. IntWriable: 表示输出键类型	

    IntWritable one= new IntWritable(1); // 定义输出值，初始始终是1
    IntWritable[] resultArr = {one, one};
    Text word = new Text(); // 定义输出键
    
    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
    	char c = 1;
    	String s = String.valueOf(c);
    	
    	String line_string = value.toString();
    	String[] sub_string_list = line_string.split(s);
    	
    	if (sub_string_list.length < 2) {
    		return;
    	}
    	
    	String guid_str = sub_string_list[1];
    	IntArrayWritable arrValue = new IntArrayWritable();    	
    	arrValue.set(resultArr);    	
    	
        word.set(guid_str);
        context.write(word, arrValue);
    }    
} // end of class

