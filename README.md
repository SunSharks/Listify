# Listify
Takes a file with poor formatted markdown checkpoint lists and formats it properly.

## Example usage
>
( ) Lorem ipsum
() dolor sit amet
[ ] consetetur sadipscing elitr
[] sed diam nonumy
- ( ) eirmod tempor
- () invidunt ut labore
-( ) et dolore magna aliquyam
-() erat, sed diam voluptua
- [] At vero eos et accusam
-[ ] et justo duo
- [] dolores et ea rebum

--> listify -->

> - [ ] Lorem ipsum
- [ ] dolor sit amet
- [ ] consetetur sadipscing elitr
- [ ] sed diam nonumy
- [ ] eirmod tempor
- [ ] invidunt ut labore
- [ ] et dolore magna aliquyam
- [ ] erat, sed diam voluptua
- [ ] At vero eos et accusam
- [ ] et justo duo
- [ ] dolores et ea rebum
