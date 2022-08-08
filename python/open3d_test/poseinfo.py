import numpy as np
# import tf
import math
# from geometry_msgs.msg import Quaternion, Point, Pose, Twist
from math import  atan2
from math import sin
from math import cos
import numpy


# epsilon for testing whether a number is close to zero
_EPS = numpy.finfo(float).eps * 4.0

def quaternion_matrix(quaternion):
    """Return homogeneous rotation matrix from quaternion.

    >>> R = quaternion_matrix([0.06146124, 0, 0, 0.99810947])
    >>> numpy.allclose(R, rotation_matrix(0.123, (1, 0, 0)))
    True

    """
    q = numpy.array(quaternion[:4], dtype=numpy.float64, copy=True)
    nq = numpy.dot(q, q)
    if nq < _EPS:
        return numpy.identity(4)
    q *= math.sqrt(2.0 / nq)
    q = numpy.outer(q, q)
    return numpy.array((
        (1.0-q[1, 1]-q[2, 2],     q[0, 1]-q[2, 3],     q[0, 2]+q[1, 3], 0.0),
        (    q[0, 1]+q[2, 3], 1.0-q[0, 0]-q[2, 2],     q[1, 2]-q[0, 3], 0.0),
        (    q[0, 2]-q[1, 3],     q[1, 2]+q[0, 3], 1.0-q[0, 0]-q[1, 1], 0.0),
        (                0.0,                 0.0,                 0.0, 1.0)
        ), dtype=numpy.float64)


def quaternion_from_matrix(matrix):
    """Return quaternion from rotation matrix.

    >>> R = rotation_matrix(0.123, (1, 2, 3))
    >>> q = quaternion_from_matrix(R)
    >>> numpy.allclose(q, [0.0164262, 0.0328524, 0.0492786, 0.9981095])
    True

    """
    q = numpy.empty((4, ), dtype=numpy.float64)
    M = numpy.array(matrix, dtype=numpy.float64, copy=False)[:4, :4]
    t = numpy.trace(M)
    if t > M[3, 3]:
        q[3] = t
        q[2] = M[1, 0] - M[0, 1]
        q[1] = M[0, 2] - M[2, 0]
        q[0] = M[2, 1] - M[1, 2]
    else:
        i, j, k = 0, 1, 2
        if M[1, 1] > M[0, 0]:
            i, j, k = 1, 2, 0
        if M[2, 2] > M[i, i]:
            i, j, k = 2, 0, 1
        t = M[i, i] - (M[j, j] + M[k, k]) + M[3, 3]
        q[i] = t
        q[j] = M[i, j] + M[j, i]
        q[k] = M[k, i] + M[i, k]
        q[3] = M[k, j] - M[j, k]
    q *= 0.5 / math.sqrt(t * M[3, 3])
    return q

def getTbc():
    T = np.array([1, 0, 0, -0.02,
          0, 0, 1,  2.15,
           0, -1, 0, 0.915,
           0, 0, 0, 1]).reshape(4,4)
    Tbc = PoseInfo().construct_fromT(T)
    return Tbc

def getgb2vbT(use_inspva = True):
    
    ypr = np.array([90, 0,0]) * math.pi/180.0
    y, p, r = ypr 
    T = euler_matrix(y, p, r)
    t = [-0.29,0.31,0.84]
    if use_inspva:
        t = [0,0,0]
    T[:3,3] = t
    return T;

def getTvbab():
    T = getgb2vbT()
    temppose = PoseInfo("Tvbab")
    temppose.construct_fromT(T)
    return temppose

def getTabvb():
   
    return getTvbab().I.set_name("Tabvb")


def euler_from_matrix(R):
    R = np.array(R)
    n = R[:, 0]
    o = R[:, 1]
    a =R[:, 2]

    y = atan2(n[1], n[0])
    p = atan2(-n[2], n[0] * cos(y) + n[1] * sin(y))
    r = atan2(a[0] * sin(y) - a[1] * cos(y), -o[0] * sin(y) + o[1] * cos(y))
    ypr = np.array([y, p, r])
    return ypr
def R2ypr(R):
    return euler_from_matrix(R)/math.pi * 180

def euler_matrix(y, p, r):
    
    Rz =[ cos(y), -sin(y), 0,
        sin(y), cos(y), 0,
        0, 0, 1]
    
    Ry = [cos(p), 0., sin(p),
        0., 1., 0.,
        -sin(p), 0., cos(p)]

    Rx = [1., 0., 0.,
        0., cos(r), -sin(r),
        0., sin(r), cos(r)]
    
    Rz = np.array(Rz).reshape(3, 3)
    Ry = np.array(Ry).reshape(3, 3)
    Rx = np.array(Rx).reshape(3, 3)
    
    R = Rz.dot(Ry).dot(Rx)
    return R
    
def ypr2R(ypr):
    ypr = np.array(ypr) / 180.0 * math.pi
    y, p, r = ypr
    return euler_matrix(y, p, r)
    
class RotationInfo(object):
    def __init__(self, name="rotation"):
        self.name = name
        return
    def construct_fromq(self, q_x,q_y,q_z,q_w):

        self.q = np.array([q_x,q_y,q_z,q_w])
        
        self.R = quaternion_matrix(self.q)
        self.ypr =  euler_from_matrix(self.R)
        self.R = self.R[:3,:3]
        return self
    def construct_fromypr(self, ypr):
        R = ypr2R(ypr)
        self.construct_fromR(R)
        return self
    def construct_fromyprradian(self, ypr):
        y, p, r = ypr
        R = euler_matrix(y, p, r)
        self.construct_fromR(R)
        return self
    def construct_fromR(self,  R = np.identity(3)):
        self.R = R.copy();
        self.ypr = np.array(R2ypr(self.R));
        self.ypr = self.ypr /180.0 * math.pi
        temp_R = np.identity(4)
        temp_R[:3,:3] = self.R
        self.q = quaternion_from_matrix(temp_R)
        return self
    def __repr__(self):
        np.set_printoptions(precision=6, suppress=True)
        res = "{}: ypr={}\nR={}".format(self.name, self.ypr * 180/math.pi , self.R)
        np.set_printoptions(suppress=True)
        return res
    @property
    def I(self):
        tempR = RotationInfo("temp")
        tempR.construct_fromR(self.R.T)
        return tempR
    def get_simple_gap(self, pose2):
        res = pose2.ypr - self.ypr
        res = res * 180/3.14
        res = "ypr={}".format(res)
        return res
        
    def __mul__(self, other):     
        if isinstance(other, RotationInfo):
            temp_R = RotationInfo("pose")
            R = self.R.dot(other.R)
            temp_R.construct_fromR(R)
            return temp_R
        else:
            return self.project_point(other)
    def project_point(self, pnt):
        pnt = np.array([pnt[0], pnt[1],pnt[2]])
        p = self.R.dot(pnt)
        return p
    def set_name(self, _name):
        self.name = _name;
        return self
        
class PoseInfo(object):
    def __init__(self, name="pose"):
        self.name = name
              
        return
    @property
    def RI(self):
        ri = RotationInfo(self.name).construct_fromq(*self.q)
        return ri
    def convert2pose(self):
        pose = Pose()
        pose.position.x, pose.position.y,pose.position.z = self.t
        pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w = self.q
        return pose
    def construct_frmxyyaw_radian(self, x_y_yaw):
        x,y,yaw = x_y_yaw
        return self.construct_fromyprradian_t([yaw, 0, 0], [x,y,0])
    def output_xy_yaw(self):
        x,y = self.t[:2]
        yaw = self.ypr[0]
        return [x,y,yaw]
        
    def construct_fromqt(self, x,y,z,q_x,q_y,q_z,q_w):
        self.t = np.array([x,y,z])
        self.q = np.array([q_x,q_y,q_z,q_w])
        
        self.R = quaternion_matrix(self.q)
        self.ypr =  euler_from_matrix(self.R)
        
      
        self.T= self.R.copy();
        self.T[:3,3] = self.t
        return self
    def construct_frompose(self, pose):
        return self.construct_pose(pose)
    def construct_pose(self, pose):
        x,y,z  = pose.position.x, pose.position.y,pose.position.z
        q_x,q_y,q_z,q_w = pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w
        self.t = np.array([x,y,z])
        self.q = np.array([q_x,q_y,q_z,q_w])
        
        self.R = quaternion_matrix(self.q)
        self.ypr =  euler_from_matrix(self.R)
        
      
        self.T= self.R.copy();
        self.T[:3,3] = self.t
        return self
    def R2ypr(self, R):
        ypr = euler_from_matrix(R)
        return ypr
    def get_short_desc(self, tree_dim = True):
        np.set_printoptions(precision=8, suppress=True)
        res = "[{:.2f}, {:.2f}, {:.2f}]".format(self.t[0], self.t[1], self.ypr[0] * 180/math.pi)
        if tree_dim:
            res = "{}: t={},yaw={}".format(self.name, self.t.transpose(), self.ypr * 180/math.pi)
        return res
    def construct_fromT(self,  _T):
        self.T = _T.copy();
        self.R = np.identity(4)
        self.R[:3,:3] = (self.T[:3,:3]).copy();
        self.t = self.T[:3, 3].copy()
        
        self.ypr = np.array(self.R2ypr(self.R));
        self.q = quaternion_from_matrix(self.R)
        return self
    def construct_fromRt(self,  R = np.identity(3), t= np.zeros(3)):
        t = np.array(t)
        self.R = np.identity(4)
        self.R[:3,:3] = R.copy();
        self.t = t.copy()
        
        self.T= self.R.copy();
        self.T[:3,3] = self.t.copy()
        
        self.ypr = np.array(self.R2ypr(self.R));
        self.q = quaternion_from_matrix(self.R)
        return self
    
    def construct_fromyprt(self,  ypr = np.zeros(3), t= np.zeros(3)):
        R = ypr2R(ypr)
        t = np.array(t)
        return self.construct_fromRt(R, t)
    def construct_fromyprradian_t(self,  ypr = np.zeros(3), t= np.zeros(3)):
        ypr = np.array(ypr)
        ypr = ypr * 180.0/math.pi
        R = ypr2R(ypr)
        t = np.array(t)
        return self.construct_fromRt(R, t)
    @property
    def I(self):
        temppose = PoseInfo("temp")
        temppose_T = (np.matrix(self.T).I).getA()
        temppose.construct_fromT(temppose_T)
        return temppose
    def get_simple_gap(self, pose2):
        res = "t={}, ypr={}".format(pose2.t - self.t, (pose2.ypr - self.ypr)* 180/math.pi)
        return res
    def get_simple_yaw_gap(self, pose2):
        np.set_printoptions(precision=8, suppress=True)
        res = "ypr={}".format((pose2.ypr - self.ypr)* 180/math.pi)
        return res
        
    def __mul__(self, other):
        
        temppose = PoseInfo("pose")
        temppose_T = (np.matrix(self.T) * np.matrix(other.T)).getA()
        temppose.construct_fromT(temppose_T)
        return temppose
    def project_point(self, pnt):
        if(len(pnt) == 2):
            pnt = [pnt[0], pnt[1], 0]
        pnt = np.array([pnt[0], pnt[1],pnt[2],  1])
        p = self.T.dot(pnt)
        p = p/p[-1]
        return p[:3]
    def set_name(self, _name):
        self.name = _name;
        return self
       

    def __repr__(self):
        np.set_printoptions(precision=6, suppress=True)
        res = "{}: t={},ypr={}\nT={}\nR={}".format(self.name, self.t, self.ypr * 180/math.pi , self.T, self.R)
        np.set_printoptions(suppress=True)
        return res
     
   
    def run(self):   
        pose = self.construct_fromqt(331383.430427,  3470499.08365, 14.7564034945,-0.00144698227995, -0.0117098317469,    0.221215935085,    0.975153473125)
        print(pose)
        return


def getgb2vbTPoseInfo(use_inspva = True):
    res = PoseInfo().construct_fromT(getgb2vbT(use_inspva = use_inspva))
    return res;

if __name__ == "__main__":   
    obj= PoseInfo("test")
    obj.run()