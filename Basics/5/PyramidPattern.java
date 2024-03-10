class PyramidPattern
{
 public static void main(String args[])
 {
  int num=5;
  int rowcount=1;
  for(int i=num;i>0;i--)
  {
   for(int k=1;k<i*2;k++)
   {
   System.out.print(" ");
   }
   for(int j=1;j<=rowcount;j++)
   {
    System.out.print(j+" ");
   }
   for(int j=rowcount-1;j>0;j--)
   {
   System.out.print(j+" ");
   }
 System.out.println();
 rowcount++;
  }
 }
} 