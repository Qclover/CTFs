#include <stdio.h>
#define KEY_LENGTH 2 // Can be anything from 1 to 13

main(){
  unsigned char ch;
  FILE *fpIn, *fpOut;
  int i;
  unsigned char key[KEY_LENGTH] = {0x00, 0x00};
  /* of course, I did not use the all-0s key to encrypt */

  fpIn = fopen("ptext.txt", "r");
  fpOut = fopen("ctext.txt", "w");

  i=0;
  while (fscanf(fpIn, "%c", &ch) != EOF) {
    /* 避免加密换行符 */  
    /* 在真实的维吉尼亚加密模式中，任何明文中的ASCII字符都将被加密，
       但是在这里，我避免加密换行符，因为这将使得解密变得更加困难... */
    if (ch!='\n') {
      fprintf(fpOut, "%02X", ch ^ key[i % KEY_LENGTH]); // ^是异或运算   
      i++;
      }
    }
 
  fclose(fpIn);
  fclose(fpOut);
  return;
} 
