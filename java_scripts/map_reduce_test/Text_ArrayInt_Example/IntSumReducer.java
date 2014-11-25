package test.map_reduce;

import java.io.IOException;
import java.lang.reflect.Array;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

// 引入hadoop的Reducer类，这个类负责MapReduce的Reduce过程。


public class IntSumReducer extends Reducer<Text, IntArrayWritable, Text, IntArrayWritable>{
	// 定义Reduce过程，也就是IntSumReducer类，这个类继承Hadoop的Reducer类。
	// 这里的”<Text,IntWritable,Text,IntWritable>”，含义跟上一节一样，依次分别是输入键类型，输入值类型，输出键类型，输出值类型。
	
	IntArrayWritable arrValue = new IntArrayWritable();

	public void reduce(Text key, Iterable<IntArrayWritable> values, Context context) throws IOException, InterruptedException {
		// 定义reduce函数。
		// key是输入键类型，values是一个实现了Iterable接口的变量，可以把它理解成values里包含若干个IntWritable整数，可以通过迭代的方式遍历所有的值
		// Context类型，跟Mapper里的Context类似的方式，是在Redurer类内部实现的。
		
		// 举例来说，假如处理一个字符串”Thisis a That isa“，那么，经过Map过程之后，到达reduce函数的时候，依次传递给reduce函数的是：key=”This”，values=<1>；key= “is”，values=<1,1>；key = “a”,values=<1, 1>；key=”That”,values=<1>。注意，在key= “is”和key=”a”的时候，values里有两个1。
		
		int data_1 = 1, data_2 = 0;		

		// Reduce过程就是用一个循环，不断从values里取值，然后累加计算和，循环结束后，将累加和赋值给result变量，然后，将键值和累加和作为一个键值对写入context。继续以上一步的例子来说，写入context的键值对依次就是<”This”，1>，<“is”，2>，<“a”,2>，<”That”, 1>。
		for(IntArrayWritable val : values) {
			// 通过val.toArray()方法取出队列中的IntWritable元素
			IntWritable[] elements = (IntWritable[])val.toArray();
			data_2 += elements[1].get();
		}
		
		IntWritable e1 = new IntWritable(data_1), e2 = new IntWritable(data_2);
		IntWritable[] resultArr = {e1, e2};
		arrValue.set(resultArr);

		context.write(key, arrValue);
	}
}
