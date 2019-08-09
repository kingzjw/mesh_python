#coding:utf-8
from Meshes import *
from Meshes import Mesh, box

def testReadSave():
    mesh = Mesh("zjw")
    path = "A.ply"
    mesh.fromPly(path)
    mesh.toObj("A.obj")
    i=10

def testCreateMesh():
    mesh = Mesh("zjw")
    mesh.addVertex([0, 0, 0])
    mesh.addVertex([0, 1, 0])
    mesh.addVertex([0, 1, 1])
    mesh.addTriangle(0,1,2)
    mesh.toObj("zjw2.obj")

if __name__ == '__main__':
    testCreateMesh()