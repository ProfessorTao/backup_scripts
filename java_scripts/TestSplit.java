// coding:utf-8

import java.io.IOException;
import java.util.StringTokenizer;
import java.io.File;
import java.io.FileInputStream;
import java.io.ByteArrayOutputStream;

public class TestSplit{
    public static String read_string(String file_path){
        try {
            File file = new File(file_path);
            FileInputStream inStream = new FileInputStream(file);
            //FileInputStream 用于读取诸如图像数据之类的原始字节流。要读取字符流，请考虑使用 FileReader。 

            ByteArrayOutputStream bos = new ByteArrayOutputStream();

            byte[] buffer = new byte[1024];
            int length = -1;

            while( (length = inStream.read(buffer)) != -1) {
                bos.write(buffer,0,length);
                // .write方法 SDK 的解释是 Writes count bytes from the byte array buffer starting at offset index to this stream.
                //  当流关闭以后内容依然存在
            }

            bos.close();
            inStream.close();

            return bos.toString();   

            // 为什么不一次性把buffer得大小取出来呢？为什么还要写入到bos中呢？ return new(buffer,"UTF-8") 不更好么?
            // return new String(bos.toByteArray(),"UTF-8");

        } catch (IOException e) {
            e.printStackTrace();
        }

        String empty_string = "";
        return empty_string;        
    }

    public static void main(String args[]) {
        String file_path = "a.txt";
        char[] c_list = {1, 2, 3};

        String delim = "";
        for (char c: c_list) {
            delim += String.valueOf(c);
        }

        String file_str = read_string(file_path);
        StringTokenizer itr = new StringTokenizer(file_str, delim);

        while(itr.hasMoreTokens()) {
            System.out.printf("%s  ", itr.nextToken());
        }

    } // end of Main

} // end of class

