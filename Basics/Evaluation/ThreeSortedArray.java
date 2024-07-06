import java.io.*;
import java.util.*;
public class ThreeSortedArray 
{
 public static void main(String[] args) {
    int num1[]={2,3,4};
    int num2[]={2,3,4};
    int num3[]={1,2,3};
    int x=0,y=0,z=0;
    ArrayList common=new ArrayList<>();
    while (x<num1.length && y<num2.length && z<num3.length) {
        if(num1[x]==num2[y] && num2[y]==num3[z])
        {
            common.add(num1[x]);
            x++;
            y++;
            z++;
        }
        else if(num1[x]<num2[y])
        {
            x++;
        }
        else if(num2[y]<num3[z])
        {
            y++;
        }
        else
        {
            z++;
        }
    }
    System.out.println("common element of three array " + common);
 }   
}
