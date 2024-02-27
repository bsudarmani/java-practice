import java.util.*;
import java.io.*;
class RandomNum2
{
    public static void main(String args[])
    {
     Scanner sc=new Scanner(System.in);
     int randnum=(int)(Math.random()*100)+1;
     int num,guessnum=0;
     do{
        System.out.println("enter the number");
         num=sc.nextInt();
         guessnum++;
         if(num>randnum)
         {
            System.out.println("too low");
         }
         else if(num<randnum){
             System.out.println("too high");
         }
     }
     while(randnum!=num);
     System.out.println("You are guessed the number  :"+ randnum + " guesses  :"+ guessnum);

    }
}