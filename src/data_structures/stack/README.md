# Stack Data Structure.
## 1 Stack là gì?
- Stack hay còn gọi là ngăn xếp hoạt động dựa trên cơ chế LIFO (Last in - First out). Cơ chế LIFO tức vào sau ra trước nghĩa là khi chúng ta thêm 1 phần tử vào trong ngăn xếp thì nó sẽ
được đặt lên đầu và đồng thời khi chúng ta muốn lấy ra thì sẽ lấy phần tử ở trên đầu ra trước rồi mới đến các phần tử phía dưới. Nó giống như  1 chồng đồng xu vậy, Chúng ta muốn lấy các đồng xu thì chúng ta sẽ lấy theo thứ tự từ trên xuống đúng không nào.
<img src="https://github.com/doctor-blue/data-structures-and-algorithms-with-Kotlin/blob/master/images/coin_stack.png" width="100" height="100" />

## 2 Implement
- Như mình đã nói ở trên chúng ta có 2 thao tác chính với ngăn xếp là thêm vào và lấy ra tương ứng với 
1. push() : Thêm một phần tử vào đầu ngăn xếp.
2. pop() : Lấy 1 phần tử ra khỏi ngăn xếp.
3. Một số hàm khác mình sẽ thêm ở phía dưới.

- Trước tiên chúng ta cần phải tạo 1 file Stack.kt và các bạn follow code ở phía dưới nha. Ở đây mình sẽ dùng ArrayList cho tiện các bạn muốn có thể sử dụng [LinkedList](https://github.com/doctor-blue/data-structures-and-algorithms-with-Kotlin/tree/master/src/data_structures/linked_list) mà mình đã hướng dẫn các bạn trong bài viết trước.
```kotlin
class Stack<T>() {
  private val storage = arrayListOf<T>()
  
  //Dưới đây mình dùng String builder nha
  override fun toString(): String = buildString {
        appendln("=====top=====")
        storage.asReversed().forEach {
            appendln("$it")
        }
        appendln("=============")
    }
}
```
### 2.1 push()
- Oke push thì đơn giản đùng không nào chúng ta chỉ cần thêm nó vào 'storage' là được rồi.
```kotlin
 fun push(element: T) {
    storage.add(element)
}
```
- Trong Main.kt các chúng ta thử push vô coi sao.
```kotlin
fun main() {
    val stack=Stack<Int>().apply {
        push(1)
        push(2)
        push(3)
        push(4)
        push(5)
    }
    println(stack)
}
```
- Sau đó chúng ta sẽ có kết quả là một stack như sau.
```
=====top=====
5
4
3
2
1
=============
```
### 2.2 pop()
- Chúng ta muốn pop 1 item ra khỏi ngăn xếp thì ta cần phải check coi 'storage' có trống hay không nếu trống chúng ta trả về null.
```kotlin
    fun pop(): T? {
        if (storage.size != 0) {
            return storage.removeAt(storage.size - 1)
        }
        return null
    }
```
- Quay lại Main.kt chúng ta thử pop 1 item ra nào.
```kotlin
fun main() {
    val stack=Stack<Int>().apply {
        push(1)
        push(2)
        push(3)
        push(4)
        push(5)
    }
    println(stack)
    val poppedElement=stack.pop()
    if (poppedElement!=null)
        println("Popped = $poppedElement")

    println(stack)
  }
```
- Và chúng ta sẽ lấy được 1 item ra khỏi stack.
```
=====top=====
5
4
3
2
1
=============

Popped = 5
=====top=====
4
3
2
1
=============
```
### 2.3 Một số hàm và thuộc tính khác giúp ngăn xếp của chúng ta dễ dùng hơn.
#### 2.3.1 Kiểm tra kích thước của stack và xem rằng stack có trống hay không.
```kotlin
val size: Int
      get() = storage.size
      
 val isEmpty: Boolean
      get() = size == 0

```
- Như vậy hàm pop() chúng ta có thể sửa thành như sau.
```kotlin
    fun pop(): T? {
        if (!isEmpty) {
            return storage.removeAt(storage.size - 1)
        }
        return null
    }
```
#### 2.3.2 create() - tạo 1 stack từ 1 Iterable (MutableList, List, ArrayList ...)
- Mình sẽ sử dụng 'companion object' ở trong chính class 'Stack' luôn nha.
```kotlin
    companion object {
        fun <T> create(list: Iterable<T>): Stack<T> {
            val stack = Stack<T>()
            list.forEach {
                stack.push(it)
            }
            return stack
        }
    }
```
- Từ một danh sách có sẵn chúng ta có thể tạo ra 1 Stack cho mình. Cùng thử ha :))) . Tại hàm main() các bạn follow thử code dưới đây.
```kotlin
   val list= listOf<String>("A","B","C","D")
    val alphabetStack=Stack.create(list)
    println(alphabetStack)
```
- Vậy là chúng ta cũng đã có 1 Stack từ 1 List có sẵn rồi.
```
=====top=====
D
C
B
A
=============
```
#### 2.3.3 stackOf() Tạo Stack từ varargs (Danh sách các đối số với số lượng tùy ý - Mình thì thường định nghĩa nó là 1 mảng các tham số tự động co dãn :v )
```kotlin
    companion object {
        fun <T> create(list: Iterable<T>): Stack<T> {
            val stack = Stack<T>()
            list.forEach {
                stack.push(it)
            }
            return stack
        }

        fun <T> stackOf(vararg item: T): Stack<T> {
            return create(item.asList())
        }
    }
```
- Như vậy là chúng ta có thể khởi tạo đầu vào 1 cách tùy ý mà không phải gọi push() nhiều lần rồi :) . Các bạn thử khởi tạo 1 stack như bên dưới trong hàm main() coi sao nha.

```kotlin
val doubleStack=Stack.stackOf(0.2,0.9,8.6,2.7,5.3)
    println(doubleStack)
```
- Output
```
=====top=====
5.3
2.7
8.6
0.9
0.2
=============
```

#### 2.3.4 peek()
- Hàm này sẽ lấy ra phần tử đầu tiên trong stack nhưng không xóa nó. Hàm này các bạn tự nghĩ cách triển khai coi sao nha !!!!

## 3 Tổng kết
- Như vậy trong bài viết này mình đã hướng dẫn các bạn implement cấu trúc dữ liệu Stack bằng cách sử dụng Kotlin. Nếu các bạn thấy những bài viết của mình có ý nghĩa thì ngại gì không cho
mình 1 star cho repo và follow mình để mình có thêm động lực viết những bài tiếp theo nhỉ ?.



