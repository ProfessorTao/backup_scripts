package test.map_reduce;

// http://www.csdn123.com/html/blogs/20131029/90249.htm


import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.ArrayWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;


public class PVUVCount {
	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		String[] otherArgs = new GenericOptionsParser(conf,args).getRemainingArgs();

		if(otherArgs.length != 2) {
			System.err.println("Usage: pvuv_count <in> <out>");
			System.exit(2);
		}
				
		int n_begin = 0, n_end = 11;
		int n_count = n_end - n_begin + 1;
		
		String base_path = otherArgs[0];
		String[] file_path_list = new String[n_count];
		
		for (int i = n_begin; i <= n_end; ++i) {
			file_path_list[i] = String.format("%s/st01-sw-dr%02d_0.txt", base_path, i);			
			System.out.println(file_path_list[i]);			
		}


		// 每个运行的处理任务就是一个Job，”pvuv_count”是Job的名字。
		Job job = new Job(conf, "pvuv_count");
		
		// Jar文件是Java语言的一个功能，可以将所有的类文件打包成一个Jar文件，setJarByClass的意思是，根据WordCount类的位置设置Jar文件。
		job.setJarByClass(PVUVCount.class);
		
		// 设置Mapper, Reducer
		job.setMapperClass(TokenizerMapper.class);
		job.setReducerClass(IntSumReducer.class);
		
		// 设置输出键的类型。
		job.setOutputKeyClass(Text.class);
		
		// 设置输出值的类型。
		job.setOutputValueClass(IntWritable.class);
		
		// 设置要处理的文件，也就是输入文件，它是otherArgs的第一个参数。
		// 设置输出文件，将处理结果写到这个文件里，它是otherArgs的第二个参数。
		for (String each_file_path:file_path_list) {
			FileInputFormat.addInputPath(job, new Path(each_file_path));
		}
		
		FileOutputFormat.setOutputPath(job, new Path(otherArgs[1]));
		
		// 最后一步，job开始执行，等待执行结束。
		System.exit(job.waitForCompletion(true)? 0 : 1);
	}
}
