from sympy import *
from sympy.vector import QuaternionOrienter


# t = symbols('t')
#
# x = sin(t)
# y = t
#
# vx = x.diff(t)
# vy = y.diff(t)
#
# yaw = atan2(vy, vx)
#
# e = yaw.diff(t)
#
# print(e)
# print(e.subs(t, 0))
# import math

class MotionCalSympy(object):
    def __init__(self):
        self.gw = Matrix([0,0,-9.81007])
        return
    def fromtwovectors(self, u, v):
        cos_theta = (u/u.norm()).dot(v/v.norm())
        half_cos = sqrt(0.5 * (1.0 + cos_theta))
        half_sin = sqrt(0.5 * (1.0 - cos_theta))
        # if Abs(half_sin) < 1e-8:
        #     return 1, 0, 0, 0
        uv_cross = u.cross(v)
        w = uv_cross/uv_cross.norm()
        
        q_w = half_cos
        q_x = w[0] * half_sin 
        q_y = w[1] * half_sin 
        q_z = w[2] * half_sin
        return Matrix([q_x,q_y,q_z, q_w])
    def specify_formula(self, t):
        
        v = 5
        acc = 0.25
        K = 2 * pi/ 10
        K2 = K*K
        ellipse_x = 3
        vz = 0
        ellipse_z = 1
        
        x =  ellipse_x * sin( K * t)
        y = v * t
        z = ellipse_z * sin( 0.5 * K * t)
        
        xyz = Matrix([x,y,z])
        vw = xyz.diff(t)
        aw = vw.diff(t)
        
        
        vb = Matrix([vw.norm(), 0, 0])
        
        q = self.fromtwovectors(vb, vw)
        
        eulerAngles = self.q2rpy(q)
        eulerAnglesRates = eulerAngles.diff(t)
        
        r, p, y= eulerAngles
        sr = sin(r)
        tp = tan(p)
        cr = cos(r)
        cp = cos(p)
        Reg = Matrix([[1, sr*tp, cr*tp],[0, cr, -sr], [0, sr/cp, cr/cp]])
        Rge = Reg.T
        
        imu_gyro = Rge * eulerAnglesRates
        
        q_sympy = QuaternionOrienter(q[3], q[0], q[1], q[2])
        Rwb = q_sympy.rotation_matrix().T
        imu_acc = Rwb.T * ( aw -  self.gw )
        
        self.expr = Matrix([[xyz], [eulerAngles], [q], [vw], [aw], [imu_gyro], [imu_acc]])
        # temp = Matrix([x,y,z])
        return self.expr
    def q2rpy(self, q):
        qx, qy, qz, qw = q
        sinr_cosp = 2 * (qw * qx + qy * qz)
        cosr_cosp = 1 - 2 * (qx * qx + qy * qy)
        roll = atan2(sinr_cosp, cosr_cosp)
        
        
        sinp = 2 * (qw * qy - qz * qx)
        # if (abs(sinp) >= 1):
        #     if sinp >=1:
        #         pitch = math.pi/2
        #     else:
        #         pitch = -math.pi
        # else:
        pitch = asin(sinp)
        
        siny_cosp = 2 * (qw * qz + qx * qy)
        cosy_cosp = 1 - 2 * (qy * qy + qz * qz)
        yaw = atan2(siny_cosp, cosy_cosp)
        
        return Matrix([roll, pitch, yaw])
    def cal(self, t_sec):
        t = symbols('t', positive=True)
        expr = self.specify_formula(t)
        # print(simplify(expr))
        
        f = lambdify(t, expr)
        print(f(t_sec))
        return
    def run(self):
        # self.cal(0.005)
        self.cal(0.475)
        return
if __name__ == "__main__":   
    obj= MotionCalSympy()
    obj.run()

