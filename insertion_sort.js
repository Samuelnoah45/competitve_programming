function insertionSort1(n, arr) {
    // Write your code here
   for(var i=n-1;i>=1;i--)
   {
       var key=arr[i];
       var j=n-1
       while(arr[j-1]>key && j-1>=0)
       {
          arr[j]=arr[j-1];
            console.log(...arr);
          j--; 
          
       }
          arr[j]=key;
            console.log(...arr)
            break;
       
       
   }

}
