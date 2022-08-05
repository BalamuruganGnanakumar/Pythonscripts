1)Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		for (int i = 0; i <= 5; i++) {
			for (int j = 0; j <= 5; j++) {
				System.out.print("*" + " ");
			}
			System.out.println();
		}
	}

}

Output:
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 

2)Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		for (int i = 1; i <= 5; i++) {
			for (int j = 1; j <= 5; j++) {
				System.out.print(i +" ");
			}
			System.out.println();
		}
	}

}

Output:
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 

3)Program:
package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		for (int i = 1; i <= 5; i++) {
			for (int j = 1; j <= 5; j++) {
				System.out.print(j +" ");
			}
			System.out.println();
		}
	}

}

Output:
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 


4)Program:
package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		for (int i = 5; i >= 0; i--) {
			for (int j = 0; j <= 5; j++) {
				System.out.print(i+" ");
			}
			System.out.println();
		}
	}

}


Output:
5 5 5 5 5 5 
4 4 4 4 4 4 
3 3 3 3 3 3 
2 2 2 2 2 2 
1 1 1 1 1 1 
0 0 0 0 0 0 


5)Program:
package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		for (int i = 1; i <= 5; i++) {
			for (int j = 5; j >= 1; j--) {
				System.out.print(j +" ");
			}
			System.out.println();
		}
	}

}

Output:
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 


6)Program:
package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		int a=1;
		for (int i = 1; i <= 5; i++) {
			for (int j = 1; j <= 5; j++) {
				System.out.print(a +" ");
				a++;
			}
			System.out.println();
		}
	}
}

Output:
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25 


7)Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		int a=1;
		for (int i = 1; i <= 5; i++) {
			for (int j = 1; j <= 5; j++) {
				System.out.print(a +" ");
				a+=2;
			}
			System.out.println();
		}
	}
}

Output:
1 3 5 7 9 
11 13 15 17 19 
21 23 25 27 29 
31 33 35 37 39 
41 43 45 47 49 


8)Program:
package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		int a=0;
		for (int i = 1; i <= 5; i++) {
			for (int j = 1; j <= 5; j++) {
				System.out.print(a +" ");
				a+=2;
			}
			System.out.println();
		}
	}
}

Output:
0 2 4 6 8 
10 12 14 16 18 
20 22 24 26 28 
30 32 34 36 38 
40 42 44 46 48 


9)Program:
package com.org.loopprog;

public class ForLoop {
public static void main(String[] args) {
		
		for (int i = 1; i <= 5; i++) {
			for (int j = 1; j <= 5; j++) {
				System.out.print(j*i +" ");
				
			}
			System.out.println();
		}
	}
}

Output:
1 2 3 4 5 
2 4 6 8 10 
3 6 9 12 15 
4 8 12 16 20 
5 10 15 20 25 


10)Program:
package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		int a=1;
		for (int i = 1; i <= 5; i++) {
			for (int j = 1; j <= 4; j++) {
				System.out.print(j +""+ i +” ");
			
			}
			System.out.println();
		}
	}
}

Output:
1 1 2 1 3 1 4 1 
1 2 2 2 3 2 4 2 
1 3 2 3 3 3 4 3 
1 4 2 4 3 4 4 4 
1 5 2 5 3 5 4 5 


11)Program:
package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		int a=1;
		for (int i = 1; i <= 5; i++) {
			for (int j = 1; j <= 4; j++) {
				System.out.print(i +""+ j +” ");
			
			}
			System.out.println();
		}
	}
}

Output:
1 1 1 2 1 3 1 4 
2 1 2 2 2 3 2 4 
3 1 3 2 3 3 3 4 
4 1 4 2 4 3 4 4 
5 1 5 2 5 3 5 4 

12)Program:
package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		int a;
		for (int i = 1; i <= 5; i++) {
			a = i;
			for (int j = 1; j <= 4; j++) {
				System.out.print(a +" ");
				a += 5;
			}
			System.out.println();
		}
	}
}


Output:
1 6 11 16 
2 7 12 17 
3 8 13 18 
4 9 14 19 
5 10 15 20 








13)Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		int a;
		int b;
		for (int i = 1; i <= 5; i++) {
			a = i;
			b = 5-i + 1;
			for (int j = 1; j <= 4; j++) {
				if (j % 2 == 1) {
					System.out.print(a +” ");
				} else {
					System.out.print(b +” ");
				}

				a = a + 5;
				b = b + 5;
			}
			System.out.println();
		}
	}
}

Output:
1 10 11 20 
2 9 12 19 
3 8 13 18 
4 7 14 17 
5 6 15 16 


14)Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
	int a;
		for (int i = 1; i <= 5; i++) {
		a = 5-i+1;	
			for (int j = 1; j <= 5; j++) {
				System.out.print(a +” ");
				a=a+5;
			}
			System.out.println();
		}
	}
}

OutPut:
5 10 15 20 25 
4 9 14 19 24 
3 8 13 18 23 
2 7 12 17 22 
1 6 11 16 21 


15)Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		int a;
		for (int i = 1; i <= 5; i++) {

			for (int j = 1; j <= 5; j++) {
				System.out.print(2 * (i + j) - 3);

			}
			System.out.println();
		}
	}
}

Output:
1 3 5 7 9 
3 5 7 9 11 
5 7 9 11 13 
7 9 11 13 15 
9 11 13 15 17 

16)Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		int a;
		for (int i = 1; i <= 5; i++) {

			for (int j = 1; j <= 5; j++) {
				System.out.print((i + j - 1)+" ");

			}
			System.out.println();
		}
	}
}

Output:
1 2 3 4 5 
2 3 4 5 6 
3 4 5 6 7 
4 5 6 7 8 
5 6 7 8 9 


17)Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		int a;
		for (int i = 1; i <= 5; i++) {

			for (int j = 1; j <= 5; j++) {
				System.out.print((i + j)%2 +" ");

			}
			System.out.println();
		}
	}
}

Output:
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 


18) Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		int a;
		for (int i = 0; i <= 5; i++) {

			for (int j = 1; j <= 5; j++) {
				System.out.print((i + j)%2);

			}
			System.out.println();
		}
	}
}

Output:
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 


19)Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		
		for (int i = 1; i <= 5; i++) {

			for (int j = 1; j <= 5; j++) {
				System.out.print((i * j)%2);

			}
			System.out.println();
		}
	}
}

Output:
10101
00000
10101
00000
10101

20)Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		
		for (int i = 1; i <= 5; i++) {

			for (int j = 0; j <= 5; j++) {
				System.out.print((i * j)%2);

			}
			System.out.println();
		}
	}
}

Output:
010101
000000
010101
000000
010101

21)Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		
		for (int i = 0; i <= 5; i++) {

			for (int j = 0; j <= 5; j++) {
				System.out.print(i%2);

			}
			System.out.println();
		}
	}
}

Output:
000000
111111
000000
111111
000000
111111

22)Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		
		for (int i = 1; i <= 5; i++) {

			for (int j = 0; j <= 5; j++) {
				System.out.print(i%2);

			}
			System.out.println();
		}
	}
}

Output:
111111
000000
111111
000000
111111

23)Program:
package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		
		for (int i = 1; i <= 5; i++) {

			for (int j = 0; j <= 5; j++) {
				System.out.print(j%2);

			}
			System.out.println();
		}
	}
}

Output:
010101
010101
010101
010101
010101

24)Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		
		for (int i = 1; i <= 5; i++) {

			for (int j = 1; j <= 5; j++) {
				System.out.print(j%2);

			}
			System.out.println();
		}
	}
}

Output:
10101
10101
10101
10101
10101

25)Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		
		for (char i = 'a'; i <= 'd'; i++) {

			for (char j = 'a'; j <= 'd'; j++) {
				System.out.print(i);

			}
			System.out.println();
		}
	}
}

Output:
aaaa
bbbb
cccc
dddd

26)Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		
		for (char i = 'a'; i <= 'd'; i++) {

			for (char j = 'a'; j <= 'd'; j++) {
				System.out.print(j);

			}
			System.out.println();
		}
	}
}

Output:
abcd
abcd
abcd
abcd

27)Program:

package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		
		for (char i = 'e'; i >= 'a'; i--) {

			for (char j = 'e'; j >= 'a'; j--) {
				System.out.print(i);

			}
			System.out.println();
		}
	}
}

Output:
eeeee
ddddd
ccccc
bbbbb
aaaaa

28)Program:
package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		
		for (char i = 'e'; i >= 'a'; i--) {

			for (char j = 'e'; j >= 'a'; j--) {
				System.out.print(j);

			}
			System.out.println();
		}
	}
}

Output:
edcba
edcba
edcba
edcba
edcba

29)Program:
package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		char c = 'a';
		char d = 'z';
		for (int i = 1; i <= 5; i++) {

			for (int j = 1; j <= 5; j++) {
				System.out.print(c);
				if (c <= d) {
					c++;
				}
			}
			System.out.println();
		}
	}
}

Output:
abcde
fghij
klmno
pqrst
uvwxy

30)Program:
package com.org.loopprog;

public class ForLoop {
	public static void main(String[] args) {
		
		for (int i = 0; i <= 4; i++) {

			for (int j = 0; j <= 4; j++) {
				System.out.print((char)(i+j+65));

			}
			System.out.println();
		}
	}
}

Output:
ABCDE
BCDEF
CDEFG
DEFGH
EFGHI













To Get particular data:

package com.org.selenium;

import java.io.IOException;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class WebTabel {
	public static void main(String[] args) throws InterruptedException, IOException {
		System.setProperty("webdriver.chrome.driver", "/Users/ezhilarasan/Desktop/bin/chromedriver");
		WebDriver dr = new ChromeDriver();
		dr.get("https://demoqa.com/webtables");
		dr.manage().window().maximize();
		WebElement find = dr.findElement(By.xpath("//div[contains(text(),'45')]"));
		String text = find.getText();
		System.out.println(text);
	}
}


To Get Row:

package com.org.selenium;

import java.io.IOException;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class WebTabel {
	public static void main(String[] args) throws InterruptedException, IOException {
		System.setProperty("webdriver.chrome.driver", "/Users/ezhilarasan/Desktop/bin/chromedriver");
		WebDriver dr = new ChromeDriver();
		dr.get("https://demoqa.com/webtables");
		dr.manage().window().maximize();
		WebElement find = dr.findElement(By.xpath("//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]"));
		String text = find.getText();
		System.out.println(text);
	}
}


To Get Header:

package com.org.selenium;

import java.io.IOException;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class WebTabel {
	public static void main(String[] args) throws InterruptedException, IOException {
		System.setProperty("webdriver.chrome.driver", "/Users/ezhilarasan/Desktop/bin/chromedriver");
		WebDriver dr = new ChromeDriver();
		dr.get("https://demoqa.com/webtables");
		dr.manage().window().maximize();
		WebElement find = dr.findElement(By.xpath("//div[@class='rt-thead -header']"));
		String text = find.getText();
		System.out.println(text);
	}
}


To get all data:

package com.org.selenium;

import java.io.IOException;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class WebTabel {
	public static void main(String[] args) throws InterruptedException, IOException {
		System.setProperty("webdriver.chrome.driver", "/Users/ezhilarasan/Desktop/bin/chromedriver");
		WebDriver dr = new ChromeDriver();
		dr.get("https://demoqa.com/webtables");
		dr.manage().window().maximize();
		WebElement find = dr.findElement(By.xpath("//div[@class='rt-tbody']"));
		String text = find.getText();
		System.out.println(text);
	}
}