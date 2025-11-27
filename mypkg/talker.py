import rclpy
from rclpy.node import Node
from person_msgs.srv import Query  # ★ サービス型をインポート

rclpy.init()
node = Node("talker")


def cb(request, response):
    # request.name に応じて response.age をセット
    if request.name == "上田隆一":
        response.age = 46
    else:
        response.age = 255

    # ログ（なくても動くけどデバッグ用に）
    node.get_logger().info(
        f"サービス呼び出し: name={request.name} → age={response.age}"
    )

    return response


def main():
    # サービス /query を作成
    srv = node.create_service(Query, "query", cb)
    node.get_logger().info("サービス /query を起動しました")
    rclpy.spin(node)

