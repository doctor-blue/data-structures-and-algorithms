# Linked List
## Khái niệm
- Danh sách liên kết là một tập hợp các dữ liệu ( các giá trị ) được sắp xếp theo một trình tự tuyến tính, một chiều. Các giá trị chính là các nút (Node) tạo thành một chuỗi. Mỗi nút gồm dữ liệu ở nút đó và tham chiếu đến nút kế tiếp trong chuỗi.
## Node
- Như mình đã nói ở trên thì mỗi Node nó sẽ làm hai nhiệm vụ: 
1. Chứa dữ liệu
2. Chứa liên kết đến Node kế tiếp hoặc đánh dấu phần cuối của danh sách

### Implement
- Trong bài này mình sẽ thực hiện implement Linked List sử dụng ngôn ngữ đó chính là Kotlin. 
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
```
