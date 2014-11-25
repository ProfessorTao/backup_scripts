package test.map_reduce;

import org.apache.hadoop.io.Writable;
import org.apache.hadoop.io.ArrayWritable;
import org.apache.hadoop.io.IntWritable;

public class IntArrayWritable extends ArrayWritable{ 
	public IntArrayWritable() { 
		super(IntWritable.class); 
	}
	
	@Override
	public String toString() {		
		Writable[] values = this.get();
		int value_length = values.length;
		
		char split_char = ' ';
	    String result = new String();	    
	    
		for (int i = 0; i < value_length; i++) {
			result += values[i].toString();
			if (i < (value_length-1)) {
				result += split_char;
			}			 
		}
		
		return result;
	}
}
