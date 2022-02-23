"""Classes for creating and working with cells of grids (and graphs)"""
from typing import Optional, Set, Tuple


class Cell() :
	def __init__(self, x = 0, y = 0, id = 0) -> None:
		self._x  = x 
		self._y  = y
		self._id = id

	def get_(self) : 
		return (self.x, self.y, self.id)


	@property
	def x(self) -> int:
		"""Return the cell's row number."""
		return self._x

	@property
	def y(self) -> int:
		"""Return the cell's column number."""
		return self._y

	@property
	def id(self) -> int:
		"""Return the cell's id."""
		return self._id

	@property
	def coordinates(self) -> Tuple[int, int]:
		"""Return the cell's row and column as a two-tuple."""
		return (self.x, self.y)
	


