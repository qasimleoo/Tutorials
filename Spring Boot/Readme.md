
## Traditional Class
class OrderService {
	private PaymentService paymentService = new PaymentService(); // Tightly Coupled
}

### Problems: 
#### DI, IoC
1. Tightly Coupled
	If you want to switch to `StripePaymentService`, you need to edit and recompile OrderService,

	`Solution: Dependency Injection`

2. Hard to Test
	You can't easily replace PaymnetService with a mock for testing. (will need class as it needs same class' object)

3. Scattered Object Creation
	Every classs creates its own objects using `new`, spearding object lifecycle and config logic throghout the app. 

All these problems can go away with the introduction of DI and IoC (IoC says take control from developer and maintain everything on your own)


# Spring Framework
It provides a comprehensive programming model for modern Java-based enterprise apps - on any kinda deploymnet platform.

It is built based on many other frameworks and tools like:

![Spring Framwork Runtime](/home/leo/RESOURCES/Spring Boot/spring-framwork.png)

---

## Spring Ecosystem

![Spring Ecosystem](/home/leo/RESOURCES/Spring Boot/spring-ecosystem.png)


---

## History of Spring Boot

![Spring Framework History](/home/leo/RESOURCES/Spring Boot/History.png)

---

# Spring Boot

Spring Framwork + Auto Configuration + Conventions + Tools

#### What it can do:
- Generative AI
- Microservices
- Reactive
- Cloud
- Web Apps
- Serverless
- Event Driven 
- Batch Processing


### Should you learn Spring (Framework) First?

- IoC and DI: @Component, @Autowired, Constructor Injection
- Bean ManagementL @Configuration, @Bean
- Spring Context: What is Application Context?
- Spring MVC, @Controller, @RestController, @RequestMapping


### Now Start Spring Boot
- Spring Boot Auto-Configuration
- Starter Dependencies
- Properties and YAML Config
- Spring Boot CLI (optional)
- SB DevTools and Actuator
- Error Handling, validation, profiles
