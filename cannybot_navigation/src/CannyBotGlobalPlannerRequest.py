#!/usr/bin/env python3

import rospy as rpy
from nav_msgs.msg import Odometry, Path
from nav_msgs.srv import GetPlan
from geometry_msgs.msg import PoseStamped


class PlannerRequest():
    """CannyBot Global Planner Request
    """

    def __init__(self):
        
        pos_topic = rpy.get_param('~pos_topic', 
                                    'base_pose_ground_truth')
        gplanner_service_name = rpy.get_param('~gplanner_service_name',
                                                '/move_base/GlobalPlanner/make_plan')
        self.map_frame_id = rpy.get_param('~frame_id', 
                                            'map')
        rate = rpy.Rate(10)
        self.current_position = Odometry()
        rpy.wait_for_message(rpy.get_namespace() + pos_topic, Odometry)
        rpy.Subscriber(rpy.get_namespace() + pos_topic, 
                        Odometry, 
                        self.current_pos)
        # Call ROS Services
        rpy.wait_for_service(gplanner_service_name)
        try:
            self.global_planner_client = rpy.ServiceProxy(gplanner_service_name, 
                                                            GetPlan)
        except rpy.ServiceException as err:
            rpy.logerr('Service call failed: %s \n %s', rpy.get_caller_id(), err)
        
        rpy.loginfo(rpy.get_caller_id() + "\n CannyBot Global Planner Request Is Running")
        rate.sleep()

    def current_pos(self, data: Odometry) -> None:
        """Callback Function for the AGV current position

        Args:
            data (Odometry): Current Position
        """
        self.current_position = data

    def global_planner_request(self, request: PoseStamped) -> Path:
        """Global Planner Request using the GPlanner client

        Args:
            request (PoseStamped): The Goal of the path

        Returns:
            Path: The generated path from start to goal
        """
        start = PoseStamped()
        start.header = self.current_position.header
        start.header.frame_id = self.map_frame_id
        start.pose = self.current_position.pose.pose
        goal = request
        goal.header = start.header
        goal.header.stamp = rpy.Time.now()
        plan_response = self.global_planner_client( start, 
                                                    goal, 
                                                    0.0)
        rpy.logdebug(rpy.get_caller_id() + "\n New Global Path is requested")
        return plan_response
    
    def plan_request (self) -> None:
        goal = PoseStamped()
        goal.pose.position.x = -1
        goal.pose.position.y = 1
        goal.pose.orientation.w = 1
        response = self.global_planner_request(goal)
        rpy.logdebug(rpy.get_caller_id() + str(response))

        
if __name__ == '__main__':
    """Initiate CannyBot Global Planner Node
    """
    rpy.init_node('cannybot_global_planner_req_node', log_level=rpy.DEBUG)
    rpy.loginfo(rpy.get_caller_id() +  '\n CannyBot Global Planner Request Node')

    Obj = PlannerRequest()
    Obj.plan_request()
    
    rpy.spin()