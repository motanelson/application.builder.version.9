exit@syscall(1);
write@syscall(4);


}
main@global(1) {
    write(1, "hello world\n", 12);
    exit(0);
}