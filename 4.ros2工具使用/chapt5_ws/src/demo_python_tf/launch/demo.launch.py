import launch
import launch_ros

def generate_launch_description():

    action_node_static_tf_broadcaster = launch_ros.actions.Node(
        package='demo_python_tf',
        executable="static_tf_broadcaster",
        output='screen',
    )
    action_node_dynamic_tf_broadcaster = launch_ros.actions.Node(
        package='demo_python_tf',
        executable="dynamic_tf_broadcaster",
        output='screen',
    )
    action_node_tf_listener = launch_ros.actions.Node(
        package='demo_python_tf',
        executable='tf_listener',
        output='both',
    )
   # 合成启动描述并返回
    launch_description = launch.LaunchDescription([
        action_node_static_tf_broadcaster,
        action_node_dynamic_tf_broadcaster,
        action_node_tf_listener
    ])
    return launch_description