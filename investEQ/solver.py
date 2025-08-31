from typing import List

from ortools.linear_solver import pywraplp

from investEQ.model.stock import Stock


class Solver:

    def __init__(
        self,
        margin: float,
        listStocks: List[Stock],
        cash: float,
        currency: str = "$",
    ):

        cashXStock = cash / len(listStocks)
        excessLowerBound = cash * margin - cash
        excessUpperBound = excessLowerBound * 1.2
        numStocks = len(listStocks)

        solver = pywraplp.Solver.CreateSolver("SCIP")

        # shares variables
        s = []
        for stock in listStocks:
            s.append(solver.IntVar(0, solver.infinity(), f"shares_{stock.ticker}"))

        # differential variables
        d = []
        for stock in listStocks:
            d.append(
                solver.NumVar(0, solver.infinity(), f"differential_{stock.ticker}")
            )

        # excessUpperBound > excess > excessLowerBound
        solver.Add(
            cash - sum(s[i] * listStocks[i].price for i in range(numStocks))
            <= excessUpperBound
        )

        solver.Add(
            cash - sum(s[i] * listStocks[i].price for i in range(numStocks))
            >= excessLowerBound
        )

        # Trick function abs() in linear programming
        for i in range(numStocks):
            solver.Add(d[i] >= s[i] * listStocks[i].price - cashXStock)
            solver.Add(d[i] >= cashXStock - s[i] * listStocks[i].price)

        z = sum(d[i] for i in range(numStocks))
        solver.Minimize(z)
        status = solver.Solve()

        if status == pywraplp.Solver.OPTIMAL:
            print("OPTIMAL SOLUTION FOUND\n")

            for i, entrada in enumerate(listStocks):
                entrada.shares = int(s[i].solution_value())

            z_value = sum(d[i].solution_value() for i in range(numStocks))

            print(f"Cash: {cash}{currency}")
            print(f"Cash per stock: {cashXStock:.2f}{currency}")
            print(f"Excess upper bound: {excessUpperBound:.2f}{currency}")
            print(f"Excess lower bound: {excessLowerBound:.2f}{currency}")
            print(
                f"Excess: {cash - sum(s[i].solution_value() * listStocks[i].price for i in range(numStocks)):.2f}{currency}"
            )
            print(f"Sum of differentials: {z_value:.2f}{currency}\n")

        elif status == pywraplp.Solver.FEASIBLE:
            print("Feasible solution found (not optimal)")
            for i, stock in enumerate(listStocks):
                stock.shares = int(s[i].solution_value())
        else:
            print(f"No solution found. Status: {status}")
