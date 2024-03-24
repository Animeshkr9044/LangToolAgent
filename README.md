# LangToolAgent
 LangChain to augment an OpenAI model with access to external tools. In particular, you'll be able to create LLM agents that use custom tools to answer user queries.


# Why do LLMs need to use Tools?

One of the most common challenges with LLMs is overcoming the lack of recency and specificity in their training data - answers can be out of date, and they are prone to hallucinations given the huge variety in their knowledge base. Tools are a great method of allowing an LLM to answer within a controlled context that draws on your existing knowledge bases and internal APIs - instead of trying to prompt engineer the LLM all the way to your intended answer, you allow it access to tools that it calls on dynamically for info, parses, and serves to customer.

Providing LLMs access to tools can enable them to answer questions with context directly from search engines, APIs or your own databases. Instead of answering directly, an LLM with access to tools can perform intermediate steps to gather relevant information. Tools can also be used in combination. For example, a language model can be made to use a search tool to lookup quantitative information and a calculator to execute calculations.