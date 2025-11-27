import rclpy
from rclpy.node import Node
from person_msgs.srv import Query  # ★ サービス型をインポート

rclpy.init()
node = Node("listener")


def main():
    # サービスのクライアントを作成
    client = node.create_client(Query, "query")

    # サービスが立ち上がるまで待つ
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info("待機中")

    # リクエスト作成
    req = Query.Request()
    req.name = "上田隆一"

    # 非同期でサービス呼び出し
    future = client.call_async(req)

    # 結果が返ってくるまで 1 回ずつ spin
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except Exception:
                node.get_logger().info("呼び出し失敗")
            else:
                node.get_logger().info(f"age: {response.age}")
            break

    node.destroy_node()
    rclpy.shutdown()

