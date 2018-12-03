#!/usr/bin/python3
class Program:
	def __init__(self,pstr):
		self.comp_stmt = CompoundStmt(pstr)
	def eval(self,state):
		self.comp_stmt.eval(state)

class CompoundStmt:
	def __init__(self,pstr):
		self.stmts = []
		for s in pstr.split(";"):
			self.stmts.append(Stmt.build(s))
	def eval(self,state):
		for s in self.stmts:
			s.eval(state)
class Stmt:
	def build(s):
		return AsgnStmt(s)

class AsgnStmt(Stmt):
	def __init__(self,s):
		v,e = s.split("=")
		self.var = v.strip()
		self.expr = Expr.build(e)
	def eval(self,state):
		state[self.var] = self.expr.eval(state)

class Expr:
	def build(s):
		s=s.strip()
		if s.find("(") >= 0 :
			return BracketExpr(s)
		elif s.find("+") >= 0:
			return PlusExpr(s)
		elif s.find("-") >= 0:
			return MinusExpr(s)
		elif s.find("*") >= 0:
			return MulExpr(s)
		elif s.find("/") >= 0:
			return DivExpr(s)
		elif s[0].isalpha():
			return VarExpr(s)
		else :
			return ConstExpr(s)

class BracketExpr(Expr):
	def __init__(self,s):
		count = 0
		i = 0
		while i!=len(s) :
			if  s[i] == '(' :
				count+=1
			if s[i] == ')' :
				count-=1 
			if (count == 1 and (s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/')) :
				opindex = i
				operator = s[i] 
			if(count == 0 and s[i] == ')') :
				end = i
			i+=1

		self.s1 = Expr.build(s[1:opindex])
		self.s2 = Expr.build(s[opindex+1:end])
		self.op = operator

	def eval(self,s):
		if self.op == '+' :
			return self.s1.eval(state) + self.s2.eval(state)
		if self.op == '-' :
			return self.s1.eval(state) - self.s2.eval(state)
		if self.op == '*' :
			return self.s1.eval(state) * self.s2.eval(state)
		if self.op == '/' :
			return int(self.s1.eval(state)/self.s2.eval(state)) 


class ConstExpr(Expr):
	def __init__(self,s):
		self.value = int(s)
	def eval(self,s):
		return self.value

class VarExpr(Expr):
	def __init__(self,s):
		self.var = s.strip()
	def eval(self,state):
		return state[self.var]

class PlusExpr(Expr):
	def __init__(self,s):
		a,b = s.split("+")
		self.l = Expr.build(a)
		self.r = Expr.build(b)
	def eval(self,state):
		return self.l.eval(state) + self.r.eval(state)

class MinusExpr(Expr):
	def __init__(self,s):
		l,r = s.split("-")
		self.l = Expr.build(l)
		self.r = Expr.build(r)
	def eval(self,state):
		return self.l.eval(state) - self.r.eval(state)

class MulExpr(Expr):
	def __init__(self,s):
		l,r = s.split("*")
		self.l = Expr.build(l)
		self.r = Expr.build(r)
	def eval(self,state):
		return self.l.eval(state) * self.r.eval(state)

class DivExpr(Expr):
	def __init__(self,s):
		l,r = s.split("/")
		self.l = Expr.build(l)
		self.r = Expr.build(r)
	def eval(self,state):
		return str(int(self.l.eval(state) / self.r.eval(state)))

p = Program("b = 6;a = b")
state = {}
p.eval(state)
print(state)
