#include <stdio.h>
#include <string.h>
int main() {
	int T,R;
	char ch1[20];
	scanf("%d", &T);
	while (T--) {
		scanf("%d %s", &R,&ch1);
		for (int k = 0; k < strlen(ch1); k++) {
			for (int i = 0; i < R; i++) {
				printf("%c", ch1[k]);
			}
		}
		printf("\n");
	}
	return 0;
}