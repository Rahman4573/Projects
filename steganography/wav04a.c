// wav04a.c - Complement LSB of each pixel of the image using exclusive-OR (^)
// Skip Header bytes (2000 bytes)
// 
# include <stdio.h>
// 
int main() {
	FILE *ifp, *ofp;
	char file1[16], file2[16];
	int c, i, nch, bitPixel, placeValu, headerSize, numColors, fileSize;
	printf("Enter the input file name: ");
	scanf("%s", file1);
// Open inut file
	if ((ifp = fopen(file1, "r")) == NULL) {
		printf("Can't open %s\n", file1);
		return 1;
	} 
	printf("Enter the Output file name: ");
	scanf("%s", file2);
// Open Output file
	if ((ofp = fopen(file2, "w")) == NULL) { 
		printf("Can't open %s\n", file2);
		return 1;		
	}
// Skip header (2000 bytes) 
	for (nch = 0; nch < 2000; nch++) {
		c = getc(ifp);
		putc(c, ofp);
	}
// Take a byte of each pixel and complement its LSB, then copy such transformed bytes to output file
	for (i = 0; i < 10; i++) {
		c = getc(ifp);
		printf("Original c = %x, ", c);
		c = c ^ 1;
		printf("c after complementing LSB = %x ---\t", c);
		putc(c, ofp);
	}
//
	while ((c = getc(ifp)) != EOF) {
		c = c ^ 1;
		putc(c, ofp);
	}
// Close output file
	fclose(ofp);
	printf("\n");
	return 0;
}

