#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main()
{
	char name[20], name2[20]; //알파벳을 저장할 변수 name2는 name의 알파벳을 담을 것
	FILE* eng; //입력 값이 저장되는 파일
	FILE* end; //문자열의 길이를 보여줄 파일

	eng = fopen("c:\\in.txt", "w"); //쓰기로 파일을 열어준다

	gets(name, sizeof(name), stdin); //입력받는다(문자열변수에, 문자열크기만큼, 표준입력으로)

	fputs(name, eng); //gets로 입력받은 문자열 변수를 eng(in파일)에 출력한다

	fclose(eng); //입력받은 파일을 닫는다

	//파일을 읽어내어 다른 파일에 불러낸다


	eng = fopen("c:\\in.txt", "r"); //입력받은 파일을 읽기로 연다
	end = fopen("c:\\out.txt", "w"); //받을 파일을 쓰기로 열어준다

	fgets(name2, sizeof(name2), eng); //파일형으로 입력받는다(name2변수에, 변수길이만큼, eng(in)파일에서)

	fprintf(end, "%s의 길이는 %d입니다.", name2, strlen(name2)); //파일형으로 해당 파일에 출력

	fclose(eng);
	fclose(end);

}