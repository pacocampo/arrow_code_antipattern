# Arrow Code Anti Pattern

This anti-pattern is named after the shape that most code makes when you have many conditionals, switch statements, or anything that allows the flow to take several paths.

If you turn your code to 180º may look like a bar graph
[![Copia-de-Captura-de-Pantalla-2021-06-02-a-la-s-16-25-24.png](https://i.postimg.cc/rpxFFHpB/Copia-de-Captura-de-Pantalla-2021-06-02-a-la-s-16-25-24.png)](https://postimg.cc/p9VtsqzC)

# Refactor Methods

Based on book: [Refactoring | Martin Fowler](https://martinfowler.com/books/refactoring.html)

1. [Guard Clauses](https://refactoring.com/catalog/replaceNestedConditionalWithGuardClauses.html)
2. [Consolidate Duplicates](https://refactoring.guru/es/consolidate-duplicate-conditional-fragments)
3. [Decompose Conditional](https://refactoring.com/catalog/decomposeConditional.html)
4. [Polymorphism](https://refactoring.com/catalog/replaceConditionalWithPolymorphism.html)