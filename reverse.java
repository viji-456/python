import java.util.*;
public class reverse {

    public static void main(String[] args){
        String s="reethu";
        String r="";
        for (int i=s.length()-1;i>=0;i--){
            r=r+s.charAt(i);
        }
        System.out.println(s);
        System.out.println(r);
    }
}