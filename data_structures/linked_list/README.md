# Linked List
## 1 Khái niệm
- Danh sách liên kết là một tập hợp các dữ liệu ( các giá trị ) được sắp xếp theo một trình tự tuyến tính, một chiều. Các giá trị chính là các nút (Node) tạo thành một chuỗi. Mỗi nút gồm dữ liệu ở nút đó và tham chiếu đến nút kế tiếp trong chuỗi.
## 2 Node
- Như mình đã nói ở trên thì mỗi Node nó sẽ làm hai nhiệm vụ: 
1. Chứa dữ liệu
2. Chứa liên kết đến Node kế tiếp hoặc đánh dấu phần cuối của danh sách
<img src="https://github.com/doctor-blue/data-structures-and-algorithms-with-Kotlin/blob/master/images/linkedList_1.PNG"/>

### 2.1 Implement
- Trong bài này mình sẽ thực hiện implement Linked List sử dụng ngôn ngữ đó chính là Kotlin. Và IDE tất nhiên là IntelliJ IDE rồi :).
- Bắt đầu chúng ta sẽ tạo 1 file Node.kt và các bạn hãy follow theo phần code dưới đây
``` kotlin
class Node<T>(var value:T,var next:Node<T>? = null) {
    override fun toString(): String {
        return if (next!=null){
            "$value -> ${next.toString()}"
        }else{
            "$value"
        }
    }
}
```
- Như mình đã nói ở trên thì Node của chúng ta có hai nhiệm vụ thì ở đây chúng ta có 2 thuộc tính đó là 'value' và 'next' trong đó 'value' là giá trị được chứa bên trong Node và 'next' chính là Node tiếp theo. Có một chút lưu ý là T là kiểu dữ liệu do chúng ta quy định.

```kotlin
fun main() {
    val node1=Node(value = 1)
    val node2=Node(value = 5)
    val node3=Node(value = 8)
    node1.next=node2
    node2.next=node3
    println(node1)
}
```
- Trên đây chúng ta tạo 3 đối tượng và liên kết chúng với nhau khi in ra chúng ta sẽ có kết quả như sau :
```
1 -> 5 -> 8
```
## 3 Implement Linked List
- Các bạn hãy tạo file LinkedList.kt follow code như dưới đây: 
``` kotlin
class LinkedList<T> {
    private var head: Node<T>? = null
    private var tail: Node<T>? = null
    var size: Int = 0

    fun isEmpty(): Boolean = size == 0
    
    override fun toString(): String {
        return if (isEmpty()) "Empty list" else head.toString()
    }
}
```
- Phía bên trên đây chúng ta có 'head' và 'tail' tương ứng với phần đầu và cuối của Linked List. Và chúng ta cũng cần có 'size' để xác định kích thước của list.
 <img src="https://github.com/doctor-blue/data-structures-and-algorithms-with-Kotlin/blob/master/images/linkedList_2.PNG" />
 
 ### 3.1 Thêm dữ liệu vào list (ở đây chính là Linked List)
 1. addToFirst() : hay còn gọi là push sẽ thêm 1 phần tử vào đầu list
 2. addToEnd() : hay còn gọi là append sẽ thêm 1 phần tử vào cuối list
 3. insert() : chúng ta có thể thêm giá trị tại bất kì vị trí nào trong list
 
 #### 3.1.1 addToFirst(value :T)
 
 ```kotlin 
     fun addToFirst(value: T): LinkedList<T> {
        //1
        head = Node(value, head)
        //2
        if (tail == null) {
            tail = head
        }
        size++
        return this
    }
 ```
 - (1) Tại đây chúng ta tạo 1 Node mới rồi gán giá trị cho 'head' với value là giá trị chúng ta truyền vào và 'next' chính là 'head' của list. Lúc này 'head' sẽ là  Node mới do chúng ta vừa tạo.
 - (2) Chúng ta cần phải check xem 'tail' nó có null hay không vì trong trường hợp list trống thì tail sẽ không nắm bất kì Node nào cả và list chỉ có 1 Node do chúng ta vừa mới tạo và nó cũng sẽ đóng vai trò vừa là 'head' vừa là 'tail' của list.
 - Ở trên mình return 'this' vì nó sẽ giúp chúng ta không cần viết code dài dòng khi ta muốn thêm giá trị một cách liên tiếp.
 - Các bạn nhớ tạo thêm 1 file Main.kt để chạy hàm main nha
 
 ```kotlin
 fun main() {
   //Create linkedList
    val linkedList = LinkedList<Int>()
    //add to first
    // nhờ return về chính nó nên chúng ta có thể thêm dữ liệu một cách liền mạch không cần lặp lại linkedList.addToFirst(value) 
    linkedList.addToFirst(1).addToFirst(3).addToFirst(-2)
    println(linkedList)
}
 ```
 - Sau khi chạy chúng ta sẽ có kết quả như sau.
 ```
 -2 -> 3 -> 1
 ```
 
  #### 3.1.2 addToEnd(value : T )
  ```kotlin 
    fun addToEnd(value: T): LinkedList<T> {
        //1
        if (isEmpty()) {
            addToFirst(value)
            return this
        }
        //2
        tail?.next = Node(value)
        //3
        tail = tail?.next
        size++
        return this

    }
  ```
  - (1) Chúng ta phải check nếu list trống thì nó giống với khi chúng ta thêm vào đầu của list nên để tận dụng code đã có chúng ta sẽ dùng lại hàm addToFirst(value).
  - (2) Vì chúng ta thêm vào cuối chúng ta sẽ tạo 1 Node mới và gán nó cho 'next' của 'tail' hiện tại, ở đây Node mới không có 'next' là bởi chúng ta thêm vào cuối mà :v.
  - (3) Ta đã thêm được vào phần cuối của list rồi nên bây giờ 'tail' mới sẽ là 'next' của 'tail' cũ.
  
  - Tại Main.kt chúng ta sẽ thêm một vài giá trị vào cuối list coi sao ha :) .
   ```kotlin
 fun main() {
   //Create linkedList
    val linkedList = LinkedList<Int>()
    //add to first
    // nhờ return về chính nó nên chúng ta có thể thêm dữ liệu một cách liền mạch không cần lặp lại linkedList.addToFirst(value) 
    linkedList.addToFirst(1).addToFirst(3).addToFirst(-2)
    
    //add to end
    linkedList.addToEnd(-32).addToEnd(5)
    
    println(linkedList)
}
 ```
 - Sau khi chạy chúng ta sẽ có kết quả
 ```
 -2 -> 3 -> 1 -> -32 -> 5
 ```
 #### 3.1.3 insert(value : T, index :Int)
 - Chúng ta khởi tạo 1 phương thức nodeAt(index:Int) để lấy ra node tại vị trí chúng ta muốn
 ```kotlin
    fun nodeAt(index: Int): Node<T>? {
        //1
        var currentNode = head
        var currentIndex = 0
        //2
        while (currentNode != null && currentIndex < index) {
            currentNode = currentNode.next
            currentIndex++
        }
        return currentNode
    }
 ```
 - (1) Ta tạo 1 tham chiếu tới 'head' để từ đây chúng ta duyệt list tới giá trị mong muốn và 'currentIndex' để theo dõi vị trí trong lúc duyệt
 - (2) Ở đây chúng ta sẽ duyệt list cho tới vị trí mong muốn hoặc khi list trống hoặc  nằm ngoài giới hạn của list tức 'currentNode' sẽ là null.
 
 - Tiếp tới sẽ là phương thức insert() của chúng ta.
 ```kotlin
 fun insert(value: T, index: Int): LinkedList<T> {
    //1
    if (index >= size-1) return addToEnd(value)

    if (index <= 0) return addToFirst(value)

    //2
    val beforeNode = nodeAt(index - 1)
    val newNode = Node(value, beforeNode?.next)
    beforeNode!!.next = newNode
    
    size++
    return this
}
 ```
 - (1) Phần này để chắc rằng khi chúng ta để index vượt quá kích thước hoặc nhập số <0 thì chúng ta đưa về hai trường hợp phía trên thêm h=vào đầu hoặc cuối list.
 - (2) Đây là phần khó hiểu nhất nên sau khi thực hiện thêm 1 số vào list tại vị trí thứ 2 như code dưới đây mình sẽ giải thích đoạn này nha.
 ```kotlin
  fun main() {
   //Create linkedList
    val linkedList = LinkedList<Int>()
    //add to first
    // nhờ return về chính nó nên chúng ta có thể thêm dữ liệu một cách liền mạch không cần lặp lại linkedList.addToFirst(value) 
    linkedList.addToFirst(1).addToFirst(3).addToFirst(-2)
    
    //add to end
    linkedList.addToEnd(-32).addToEnd(5)
    //insertAt
    linkedList.insert(82,2)
    println(linkedList)
}
 ```
 - Kết quả của đoạn trên chúng ta sẽ có là :
 ```
 -2 -> 3 -> 82 -> 1 -> -32 -> 5
 ```
 - Như mình đã nói thì mình sẽ giải thích đoạn code tại (2).
 ```
 list ban đầu ta có là :  -2 -> 3 -> 1 -> -32 -> 5
 Chúng ta cần thêm 82 vào vị trí thứ 2 trong list nên trước tiên chúng ta phải lấy ra node đứng trước vị trí 2 ra (node 1) và nó có giá trị là '3 -> 1 -> -32 -> 5' và gán cho beforeNode.
 Sau đó chúng ta tạo 1 Node mới có value do chúng ta truyền vào ( value = 82) và 'next' sẽ là 'next' của beforeNode (node ở vị trí thứ 1) có giá trị là '1 -> -32 -> 5'.
 Tiếp theo ta gán lại 'next' của beforeNode (node ở vị trí 1) là Node mới do chúng ta mới tạo ra ở trên ( có giá trị lúc này là 8-> 1 -> -32 -> 5).
 Như vậy chúng ta đã thêm được 82 vào list tại vị trí thứ 2.
 ```
 - Phần này mình khuyên các bạn nên chịu khó debug ha sẽ rõ hơn rất nhiều mình giải thích đó :v ( Mình đã cố hết sức rồi nhưng năng lực chưa đủ :))) )
 
 ### 3.2 Xóa dữ liệu khỏi list ( list ở đây chính là LinkedList )
 1. pop() : Xóa dữ liệu tại đầu danh sách
 2. removeLast() : Xóa dữ liệu ở cuối danh sách.
 3. removeAt() : Xóa dữ liệu tại vị trí bất kì ( Để thêm phần hấp dẫn cho bài viết mình nghĩ các bạn nên cố gắng tìm cách làm nha - Chia sẻ của 1 anh bạn lười nhác nào đó :) )
 #### 3.2.1 pop()
 ```kotlin
    fun pop(): T? {
        if (!isEmpty()) size--

        val result = head?.value
        head = head?.next
        if (isEmpty()) tail = null

        return result
    }
 ```
 - Phần này khá dễ hiểu đúng không chúng ta lấy giá trị đầu ra và xóa nó khỏi list thì đơn giản chúng ta chỉ cần gán 'head' của list là node tiếp theo thôi đúng không 'head?.next'.
 
  ```kotlin
  fun main() {
   //Create linkedList
    val linkedList = LinkedList<Int>()
    //add to first
    // nhờ return về chính nó nên chúng ta có thể thêm dữ liệu một cách liền mạch không cần lặp lại linkedList.addToFirst(value) 
    linkedList.addToFirst(1).addToFirst(3).addToFirst(-2)
    
    //add to end
    linkedList.addToEnd(-32).addToEnd(5)
    //insertAt
    linkedList.insert(82,2)
    
    //pop
    val poppedValue = linkedList.pop()
    
    println(linkedList)
}
 ```
 - poppedValue chính là giá trị chúng ta lấy ra khỏi list đó (poppedValue= -2).
 
 #### 3.2.2 removeLast()
 ```kotlin
   fun removeLast(): T? {
        //1
        val head = head ?: return null
        if (head.next == null) return pop()

        size--
        //2
        var pre = head
        var current = head

        var next = current.next
        while (next != null) {
            pre = current
            current = next
            next = current.next
        }
        //3
        pre.next = null
        tail = pre
        return current.value
    }
 ```
 - (1) Chúng ta cần lấy 'head' ra nếu trong trường hợp list trống ( 'head' là null ) hoặc khi chỉ có 1 node ( head.next = null) thì chúng ta sử dụng lại pop() để tận dụng lại code.
 - (2) Ở đây ta phải tìm được đến phần tử cuối cùng của list và phần tử kế cuối ( nếu bạn hỏi sao không dùng nodeAt() để lấy 2 phần tử này thì 1 vòng lặp đương nhiên sẽ bớt phức tạp hơn 2 mà đúng không nhỉ ? )
 - (3) Ta sẽ gán 'next' của phần tử kế cuối là null và nó cũng sẽ đóng vai trò là 'tail' của list luôn vì chúng ta bỏ phần tử cuối mà đúng không :).
 
 - Tại Main.kt
  ```kotlin
  fun main() {
   //Create linkedList
    val linkedList = LinkedList<Int>()
    //add to first
    // nhờ return về chính nó nên chúng ta có thể thêm dữ liệu một cách liền mạch không cần lặp lại linkedList.addToFirst(value) 
    linkedList.addToFirst(1).addToFirst(3).addToFirst(-2)
    
    //add to end
    linkedList.addToEnd(-32).addToEnd(5)
    //insertAt
    linkedList.insert(82,2)
    
    //pop
    val poppedValue = linkedList.pop()
    
     //remove last
    val removedValue = linkedList.removeLast()
    
    println(linkedList)
}
 ```
 - removedValue sẽ là giá trị cuối cùng của list trước khi xóa ( removedValue =5 ).
 
 #### 3.2.3 removeAt() 
 - NO NO NO cái này các bạn cố gắng tìm hiểu và thực hiện nha 
 
 
 ## 4 Tổng kết
 - Hi vọng thông qua bài viết này mình đã giúp các bạn thực hiện cấu trúc dữ liệu Linked List bằng cách sử dụng Kotlin và nếu các bạn thấy nó hay và có ích tại sao lại tiếc 1 sao cho project và 1 follow cho mình nhỉ ahihi !!!!!
 
