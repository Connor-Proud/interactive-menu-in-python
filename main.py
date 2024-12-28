import keyboard
from colorama import Fore, Back
import os
from os import system
import time

def clear():
    os.system("cls")

state_converter={0:"Lamborghini",
                 1:"Ferrari",
                 2:"McLaren"
                }

def lam_menu(state, previous_state):
    if state != previous_state:
        clear()
        if state == 0:
            print(f"{Fore.BLACK}{Back.WHITE}|[ Aventador ]|{Fore.RESET}{Back.RESET}\n|[ Huracán EVO ]|\n|[ Urus ]|\n|[ Huracán STO ]|\n|[ Sián FKP 37 ]|")
            while True:
                if keyboard.is_pressed("space"):
                    clear()
                    print("""Price: $500,000
- Engine: 6.5L V12
- Top Speed: 217 mph
- Description: DESIGNED TO PUSH BEYOND PERFORMANCE:
    Revolutionary thinking is at the heart of every idea from Automobili Lamborghini.
    Whether it is aerospace-inspired design or technologies
    applied to the naturally aspirated V12 engine or carbon-fiber
    structure, going beyond accepted limits is part of our philosophy.
    The Aventador advances every concept of performance, immediately establishing
    itself as the benchmark for the super sports car sector. Giving a glimpse of the
    future today, it comes from a family of supercars already considered legendary. 
    Each and every detail of the Aventador bears the hallmarks of the House of the 
    Raging Bull. It is a true masterpiece of design that expresses dynamism and power,
    with the carbon-fiber monocoque the jewel in its crown. The interior combines
    high-level technology and luxury equipment, crafted by skilled artisans""")
                    print("\npress (enter) to return, wait 2 seconds then press (down arrow).")
                    while True:
                        if keyboard.is_pressed("enter"):
                            continue
                elif keyboard.is_pressed("up") or keyboard.is_pressed("down"):
                    break
                        
        elif state == 1:
            print(f"|[ Aventador ]|\n{Fore.BLACK}{Back.WHITE}|[ Huracán EVO ]|{Fore.RESET}{Back.RESET}\n|[ Urus ]|\n|[ Huracán STO ]|\n|[ Sián FKP 37 ]|")
            while True:
                if keyboard.is_pressed("space"):
                    clear()
                    print("""Price: $261,274
- Engine: 5.2L V10
- Top Speed: 202 mph
- Description: REDEFINING THE ART OF DRIVING:
    The Lamborghini Huracán EVO is the evolution of the most successful V10-powered 
    Lamborghini. The EVO showcases refined aerodynamics, cutting-edge technology, 
    and iconic design, making it a true driver-focused masterpiece. With its naturally 
    aspirated 5.2L V10 engine, recalibrated to unleash even greater power, and 
    the Lamborghini Dinamica Veicolo Integrata (LDVI) system, the Huracán EVO ensures 
    unparalleled responsiveness and control.
    Its striking exterior features new front and rear bumpers and enhanced airflow 
    dynamics, while the luxurious interior boasts cutting-edge infotainment, premium 
    materials, and meticulous craftsmanship. Every detail has been designed to deliver 
    a driving experience that is as thrilling as it is unforgettable.
    Experience the perfect fusion of innovation, performance, and style with the 
    Lamborghini Huracán EVO.""")
                    print("\npress (enter) to return, wait 2 seconds then press (down arrow).")
                    while True:
                        if keyboard.is_pressed("enter"):
                            continue
                elif keyboard.is_pressed("up") or keyboard.is_pressed("down"):
                    break

        elif state == 2:
            print(f"|[ Aventador ]|\n|[ Huracán EVO ]|\n{Fore.BLACK}{Back.WHITE}|[ Urus ]|{Fore.RESET}{Back.RESET}\n|[ Huracán STO ]|\n|[ Sián FKP 37 ]|")
            while True:
                if keyboard.is_pressed("space"):
                    clear()
                    print("""Price: $225,000
- Engine: 4.0L Twin-Turbo V8
- Top Speed: 190 mph
- Description: THE WORLD'S FIRST SUPER SUV:
    The Lamborghini Urus is a visionary vehicle that combines the soul of a supercar 
    with the functionality of an SUV. With its powerful 4.0L twin-turbo V8 engine, 
    the Urus delivers 641 horsepower and 0-60 mph acceleration in just 3.6 seconds. 
    Its striking design is unmistakably Lamborghini, featuring aggressive lines and 
    a commanding presence.
    Inside, the Urus blends luxury and technology with premium materials, advanced 
    infotainment, and customizable driving modes. Whether on the road, track, or 
    off-road terrain, the Urus provides unparalleled versatility and performance.
    Designed to conquer every journey, the Lamborghini Urus redefines what an SUV 
    can be, offering an exhilarating driving experience for those who demand 
    performance and practicality.""")
                    print("\npress (enter) to return, wait 2 seconds then press (down arrow).")
                    while True:
                        if keyboard.is_pressed("enter"):
                            continue
                elif keyboard.is_pressed("up") or keyboard.is_pressed("down"):
                    break
                
        elif state == 3:
            print(f"|[ Aventador ]|\n|[ Huracán EVO ]|\n|[ Urus ]|\n{Fore.BLACK}{Back.WHITE}|[ Huracán STO ]|{Fore.RESET}{Back.RESET}\n|[ Sián FKP 37 ]|")
            while True:
                if keyboard.is_pressed("space"):
                    clear()
                    print("""Price: $327,838
- Engine: 5.2L V10
- Top Speed: 193 mph
- Description: THE PUREST ESSENCE OF LAMBORGHINI:
    The Lamborghini Huracán STO (Super Trofeo Omologata) is a street-legal race car 
    inspired by Lamborghini’s racing heritage. With its naturally aspirated 5.2L V10 
    engine producing 640 horsepower, the Huracán STO delivers exhilarating performance, 
    accelerating from 0 to 60 mph in just 3.0 seconds.
    Designed with a focus on lightweight materials and aerodynamics, the STO features 
    a distinctive exterior with an integrated rear shark fin, prominent air ducts, and 
    advanced aerodynamic elements for superior downforce and control. Inside, it boasts 
    race-inspired design with Alcantara and carbon fiber finishes, complemented by 
    cutting-edge technology.
    Perfectly blending the excitement of motorsport with the thrill of the road, the 
    Huracán STO provides an unmatched driving experience for true enthusiasts.""")
                    print("\npress (enter) to return, wait 2 seconds then press (down arrow).")
                    while True:
                        if keyboard.is_pressed("enter"):
                            continue
                elif keyboard.is_pressed("up") or keyboard.is_pressed("down"):
                    break
                
        elif state == 4:
            print(f"|[ Aventador ]|\n|[ Huracán EVO ]|\n|[ Urus ]|\n|[ Huracán STO ]|\n{Fore.BLACK}{Back.WHITE}|[ Sián FKP 37 ]|{Fore.RESET}{Back.RESET}")
            while True:
                if keyboard.is_pressed("space"):
                    clear()
                    print("""Price: $3,700,000
- Engine: 6.5L V12 + 48V Electric Motor
- Top Speed: 217 mph
- Description: A MASTERPIECE OF INNOVATION:
    The Lamborghini Sián FKP 37 is a revolutionary hybrid supercar, blending the iconic 
    6.5L naturally aspirated V12 engine with a groundbreaking 48V electric motor. This 
    cutting-edge powertrain delivers a combined output of 819 horsepower, propelling 
    the Sián from 0 to 60 mph in just 2.8 seconds.
    As Lamborghini’s first hybrid, the Sián incorporates innovative supercapacitor 
    technology for unparalleled energy storage and efficiency. Its futuristic design 
    showcases sharp lines, an iconic Y-shaped lighting signature, and exclusive aerodynamic 
    elements that enhance performance.
    Limited to just 63 units, the Sián FKP 37 represents the pinnacle of Lamborghini’s 
    engineering and design prowess, offering an unparalleled blend of power, technology, 
    and exclusivity for discerning collectors and enthusiasts.""")
                    print("\npress (enter) to return, wait 2 seconds then press (down arrow).")
                    while True:
                        if keyboard.is_pressed("enter"):
                            continue
                elif keyboard.is_pressed("up") or keyboard.is_pressed("down"):
                    break

def fer_menu(state, previous_state):
    if state != previous_state:
        clear()
        if state == 0:
            print(f"{Fore.BLACK}{Back.WHITE}|[ Roma ]|{Fore.RESET}{Back.RESET}\n|[ F8 Tributo ]|\n|[ SF90 Stradale ]|\n|[ 812 Superfast ]|\n|[ Portofino M ]|")
            while True:
                if keyboard.is_pressed("space"):
                    clear()
                    print("""Price: $243,360
- Engine: 3.9L Twin-Turbo V8
- Top Speed: 199 mph
- Description: LA NUOVA DOLCE VITA:
    The Ferrari Roma is a contemporary representation of timeless Italian elegance. 
    With its sleek and minimalist design, the Roma embodies a perfect blend of 
    performance, luxury, and refinement. Powered by a 3.9L twin-turbo V8 engine 
    producing 612 horsepower, the Roma accelerates from 0 to 60 mph in just 3.4 seconds.
    The exterior design features flowing lines, an aerodynamic silhouette, and a 
    modern take on Ferrari’s classic aesthetics. Inside, the Roma offers a luxurious 
    cabin with state-of-the-art technology, premium materials, and a driver-focused 
    layout.
    Celebrating the joy of driving, the Ferrari Roma is a testament to Ferrari’s 
    ability to combine effortless performance with unparalleled sophistication.""")
                    print("\npress (enter) to return, wait 2 seconds then press (down arrow).")
                    while True:
                        if keyboard.is_pressed("enter"):
                            continue
                elif keyboard.is_pressed("up") or keyboard.is_pressed("down"):
                    break
                
        elif state == 1:
            print(f"|[ Roma ]|\n{Fore.BLACK}{Back.WHITE}|[ F8 Tributo ]|{Fore.RESET}{Back.RESET}\n|[ SF90 Stradale ]|\n|[ 812 Superfast ]|\n|[ Portofino M ]|")
            while True:
                if keyboard.is_pressed("space"):
                    clear()
                    print("""Price: $283,950
- Engine: 3.9L Twin-Turbo V8
- Top Speed: 211 mph
- Description: A CELEBRATION OF EXCELLENCE:
    The Ferrari F8 Tributo pays homage to Ferrari’s iconic V8 lineage, representing 
    the pinnacle of performance and design. Powered by a 3.9L twin-turbo V8 engine 
    delivering an astounding 710 horsepower, the F8 Tributo rockets from 0 to 60 mph 
    in just 2.9 seconds.
    Its design is a seamless blend of aerodynamics and aesthetics, featuring 
    sculpted lines, a signature S-duct for improved downforce, and a Lexan rear 
    screen showcasing the V8 engine. Inside, the cockpit combines race-inspired 
    ergonomics with luxurious materials and cutting-edge technology.
    The F8 Tributo is a masterpiece of engineering and artistry, offering an 
    exhilarating driving experience that celebrates Ferrari’s unparalleled heritage 
    and innovation.""")
                    print("\npress (enter) to return, wait 2 seconds then press (down arrow).")
                    while True:
                        if keyboard.is_pressed("enter"):
                            continue
                elif keyboard.is_pressed("up") or keyboard.is_pressed("down"):
                    break
                
        elif state == 2:
            print(f"|[ Roma ]|\n|[ F8 Tributo ]|\n{Fore.BLACK}{Back.WHITE}|[ SF90 Stradale ]|{Fore.RESET}{Back.RESET}\n|[ 812 Superfast ]|\n|[ Portofino M ]|")
            while True:
                if keyboard.is_pressed("space"):
                    clear()
                    print("""Price: $507,000
- Engine: 4.0L Twin-Turbo V8 + 3 Electric Motors
- Top Speed: 211 mph
- Description: THE FUTURE OF PERFORMANCE:
    The Ferrari SF90 Stradale marks a new chapter in Ferrari’s history as its first 
    plug-in hybrid supercar. Combining a 4.0L twin-turbo V8 engine with three electric 
    motors, the SF90 Stradale delivers an extraordinary 986 horsepower, achieving 
    0-60 mph in a blistering 2.5 seconds.
    Its design reflects the pinnacle of aerodynamics and innovation, featuring sleek 
    lines, an active rear spoiler, and a futuristic cockpit that seamlessly integrates 
    luxury and cutting-edge technology. The SF90 Stradale offers multiple driving 
    modes, including a pure electric mode for up to 15.5 miles of zero-emissions driving.
    Representing Ferrari’s dedication to pushing the boundaries of performance and 
    technology, the SF90 Stradale is a true masterpiece for the modern era.""")
                    print("\npress (enter) to return, wait 2 seconds then press (down arrow).")
                    while True:
                        if keyboard.is_pressed("enter"):
                            continue
                elif keyboard.is_pressed("up") or keyboard.is_pressed("down"):
                    break
                
        elif state == 3:
            print(f"|[ Roma ]|\n|[ F8 Tributo ]|\n|[ SF90 Stradale ]|\n{Fore.BLACK}{Back.WHITE}|[ 812 Superfast ]|{Fore.RESET}{Back.RESET}\n|[ Portofino M ]|")
            while True:
                if keyboard.is_pressed("space"):
                    clear()
                    print("""Price: $405,450
- Engine: 6.5L Naturally Aspirated V12
- Top Speed: 211 mph
- Description: THE ULTIMATE EXPRESSION OF V12 PERFORMANCE:
    The Ferrari 812 Superfast is a celebration of Ferrari’s unparalleled V12 heritage, 
    delivering breathtaking performance and exhilarating driving dynamics. Equipped 
    with a 6.5L naturally aspirated V12 engine producing 789 horsepower, the 812 
    Superfast accelerates from 0 to 60 mph in just 2.9 seconds.
    Its aggressive yet elegant design features aerodynamic enhancements, sculpted lines, 
    and a commanding presence on the road. The cockpit combines luxurious materials 
    with a driver-centric layout, incorporating advanced technology to enhance the 
    driving experience.
    As the fastest and most powerful front-engined Ferrari ever built, the 812 
    Superfast offers a perfect blend of speed, style, and sophistication, embodying 
    the essence of Ferrari’s engineering excellence.""")
                    print("\npress (enter) to return, wait 2 seconds then press (down arrow).")
                    while True:
                        if keyboard.is_pressed("enter"):
                            continue
                elif keyboard.is_pressed("up") or keyboard.is_pressed("down"):
                    break
                
        elif state == 4:
            print(f"|[ Roma ]|\n|[ F8 Tributo ]|\n|[ SF90 Stradale ]|\n|[ 812 Superfast ]|\n{Fore.BLACK}{Back.WHITE}|[ Portofino M ]|{Fore.RESET}{Back.RESET}")
            while True:
                if keyboard.is_pressed("space"):
                    clear()
                    print("""Price: $226,000
- Engine: 3.9L Twin-Turbo V8
- Top Speed: 199 mph
- Description: THE EVOLUTION OF LUXURY AND PERFORMANCE:
    The Ferrari Portofino M is the epitome of luxury and performance in Ferrari’s 
    grand touring lineup. Powered by a 3.9L twin-turbo V8 engine producing 612 horsepower, 
    the Portofino M delivers a thrilling driving experience with a 0-60 mph time of 
    just 3.1 seconds. 
    The Portofino M is equipped with Ferrari’s innovative 8-speed dual-clutch transmission, 
    offering seamless gear shifts and enhanced driving dynamics. Its striking exterior 
    combines elegance with sportiness, while the interior exudes luxury with fine 
    materials, a sophisticated infotainment system, and a driver-focused layout.
    With increased power, sharper handling, and refined styling, the Portofino M represents 
    the next chapter in Ferrari’s grand touring heritage, offering an ideal balance of 
    everyday usability and high-performance thrills.""")
                    print("\npress (enter) to return, wait 2 seconds then press (down arrow).")
                    while True:
                        if keyboard.is_pressed("enter"):
                            continue
                elif keyboard.is_pressed("up") or keyboard.is_pressed("down"):
                    break

def mcl_menu(state, previous_state):
    if state != previous_state:
        clear()
        if state == 0:
            print(f"{Fore.BLACK}{Back.WHITE}|[ Artura ]|{Fore.RESET}{Back.RESET}\n|[ 720S ]|\n|[ 570S ]|\n|[ 765LT ]|\n|[ GT ]|")
            while True:
                if keyboard.is_pressed("space"):
                    clear()
                    print("""Price: $225,000
- Engine: 3.0L Twin-Turbo V6 + Electric Motor
- Top Speed: 205 mph
- Description: THE FUTURE OF SUPER CAR PERFORMANCE:
    The McLaren Artura is a revolutionary hybrid supercar, combining a 3.0L twin-turbo V6 
    engine with an electric motor to produce a total of 671 horsepower. This cutting-edge powertrain 
    propels the Artura from 0 to 60 mph in just 3.0 seconds, offering electrifying acceleration 
    and remarkable efficiency.
    The Artura is built on McLaren’s lightweight Carbon Lightweight Architecture (MCLA), ensuring 
    a perfect balance of performance, agility, and handling. Its aerodynamically optimized exterior 
    features sharp lines and a distinctive design, while the interior is focused on driver engagement, 
    offering a modern cockpit with advanced digital displays and premium materials.
    As McLaren’s first plug-in hybrid, the Artura represents a bold step into the future of supercar 
    performance, offering the thrill of a supercar with the added efficiency and performance 
    of hybrid technology.""")
                    print("\npress (enter) to return, wait 2 seconds then press (down arrow).")
                    while True:
                        if keyboard.is_pressed("enter"):
                            continue
                elif keyboard.is_pressed("up") or keyboard.is_pressed("down"):
                    break
                
        elif state == 1:
            print(f"|[ Artura ]|\n{Fore.BLACK}{Back.WHITE}|[ 720S ]|{Fore.RESET}{Back.RESET}\n|[ 570S ]|\n|[ 765LT ]|\n|[ GT ]|")
            while True:
                if keyboard.is_pressed("space"):
                    clear()
                    print("""Price: $299,000
- Engine: 4.0L Twin-Turbo V8
- Top Speed: 212 mph
- Description: THE ULTIMATE SUPERCAR EXPERIENCE:
    The McLaren 720S is a stunning example of automotive engineering, combining blistering performance 
    with striking design. Powered by a 4.0L twin-turbo V8 engine delivering 710 horsepower, the 720S 
    accelerates from 0 to 60 mph in just 2.7 seconds, pushing the boundaries of speed and precision.
    The design of the 720S is focused on aerodynamic efficiency, featuring active aerodynamics and 
    sculpted bodywork that enhances downforce while minimizing drag. Its lightweight carbon-fiber 
    construction ensures agility and performance, making it one of the most dynamic supercars on the road.
    Inside, the cockpit offers a minimalist design with a focus on the driving experience, featuring 
    advanced digital displays and premium materials that create a perfect harmony of luxury and function.
    With its remarkable power, advanced technology, and breathtaking handling, the McLaren 720S is 
    a true embodiment of the supercar spirit.""")
                    print("\npress (enter) to return, wait 2 seconds then press (down arrow).")
                    while True:
                        if keyboard.is_pressed("enter"):
                            continue
                elif keyboard.is_pressed("up") or keyboard.is_pressed("down"):
                    break
                
        elif state == 2:
            print(f"|[ Artura ]|\n|[ 720S ]|\n{Fore.BLACK}{Back.WHITE}|[ 570S ]|{Fore.RESET}{Back.RESET}\n|[ 765LT ]|\n|[ GT ]|")
            while True:
                if keyboard.is_pressed("space"):
                    clear()
                    print("""Price: $192,500
- Engine: 3.8L Twin-Turbo V8
- Top Speed: 204 mph
- Description: A PURE SUPER CAR EXPERIENCE:
    The McLaren 570S offers a perfect introduction to McLaren’s exceptional performance 
    and innovative engineering. Powered by a 3.8L twin-turbo V8 engine producing 562 horsepower, 
    the 570S accelerates from 0 to 60 mph in just 3.1 seconds, delivering a thrilling driving experience.
    Its lightweight carbon-fiber monocoque construction ensures exceptional agility and handling, 
    while the aerodynamic design enhances both performance and visual appeal. 
    Inside, the 570S features a refined interior with a focus on driver engagement, 
    combining premium materials with a minimalist layout that places control in the hands of the driver.
    A true everyday supercar, the McLaren 570S balances practicality with the performance 
    and precision expected from a McLaren.""")
                    print("\npress (enter) to return, wait 2 seconds then press (down arrow).")
                    while True:
                        if keyboard.is_pressed("enter"):
                            continue
                elif keyboard.is_pressed("up") or keyboard.is_pressed("down"):
                    break
                
        elif state == 3:
            print(f"|[ Artura ]|\n|[ 720S ]|\n|[ 570S ]|\n{Fore.BLACK}{Back.WHITE}|[ 765LT ]|{Fore.RESET}{Back.RESET}\n|[ GT ]|")
            while True:
                if keyboard.is_pressed("space"):
                    clear()
                    print("""Price: $358,000
- Engine: 4.0L Twin-Turbo V8
- Top Speed: 205 mph
- Description: A MASTERPIECE OF PERFORMANCE:
    The McLaren 765LT takes the art of performance to the next level. Powered by a 4.0L 
    twin-turbo V8 engine producing an astonishing 755 horsepower, the 765LT accelerates 
    from 0 to 60 mph in just 2.7 seconds, delivering a truly breathtaking driving experience. 
    With a focus on weight reduction, the 765LT features an extensive use of lightweight 
    materials, making it one of the most agile and focused supercars on the road.
    The exterior design is aggressive yet refined, with active aerodynamics and a striking 
    rear wing that maximizes downforce. Inside, the 765LT offers a performance-oriented 
    cockpit, with minimal luxury but maximized driving engagement and advanced technology.
    A limited production model, the 765LT represents the pinnacle of McLaren’s engineering, 
    combining extreme performance with precision handling, making it one of the most capable 
    track-focused supercars ever built.""")
                    print("\npress (enter) to return, wait 2 seconds then press (down arrow).")
                    while True:
                        if keyboard.is_pressed("enter"):
                            continue
                elif keyboard.is_pressed("up") or keyboard.is_pressed("down"):
                    break
                
        elif state == 4:
            print(f"|[ Artura ]|\n|[ 720S ]|\n|[ 570S ]|\n|[ 765LT ]|\n{Fore.BLACK}{Back.WHITE}|[ GT ]|{Fore.RESET}{Back.RESET}")
            while True:
                if keyboard.is_pressed("space"):
                    clear()
                    print("""Price: $210,000
- Engine: 4.0L Twin-Turbo V8
- Top Speed: 203 mph
- Description: THE ULTIMATE GRAND TOURER:
    The McLaren GT redefines the grand tourer segment, combining exceptional performance 
    with supreme comfort and luxury. Powered by a 4.0L twin-turbo V8 engine producing 
    612 horsepower, the GT delivers effortless acceleration, going from 0 to 60 mph in just 
    3.1 seconds, while maintaining a smooth, refined ride.
    Designed for long-distance drives, the McLaren GT offers a spacious and luxurious 
    cabin, featuring premium materials and advanced technology. The sleek exterior design 
    is both aerodynamic and elegant, while the rear offers an expansive trunk for everyday 
    usability, making it the perfect car for both performance enthusiasts and those 
    seeking a more comfortable, practical supercar.
    With a focus on both speed and comfort, the McLaren GT brings a new level of versatility 
    to McLaren's performance range, offering an unrivaled driving experience for both the road 
    and the open highway.\n""")
                    print("\npress (enter) to return, wait 2 seconds then press (down arrow).")
                    while True:
                        if keyboard.is_pressed("enter"):
                            continue
                elif keyboard.is_pressed("up") or keyboard.is_pressed("down"):
                    break

def print_menu(state, previous_state):
    if state != previous_state:
        clear()
        if state == 0:
            print(f"{Fore.BLACK}{Back.WHITE}|[ Lamborghini ]|{Fore.RESET}{Back.RESET}\n|[ Ferrari ]|\n|[ McLaren ]|")
        elif state == 1:
            print(f"|[ Lamborghini ]|\n{Fore.BLACK}{Back.WHITE}|[ Ferrari ]|{Fore.RESET}{Back.RESET}\n|[ McLaren ]|")
        elif state == 2:
            print(f"|[ Lamborghini ]|\n|[ Ferrari ]|\n{Fore.BLACK}{Back.WHITE}|[ McLaren ]|{Fore.RESET}{Back.RESET}")

def main():
    system("toggle.fullscreen")
    state = 0
    previous_state = -1; change_in_state=0
    lam_state = 0; lam_previous_state = -1
    fer_state = 0; fer_previous_state = -1
    mcl_state = 0; mcl_previous_state = -1
    while True:
        if change_in_state == 0:
            print_menu(state, previous_state)
            previous_state = state
            if keyboard.is_pressed("up"):
                time.sleep(0.2)
                state = (state - 1) % 3
            elif keyboard.is_pressed("down"):
                time.sleep(0.2)
                state = (state + 1) % 3
            elif keyboard.is_pressed("enter"):
                change_in_state = 1                
        elif change_in_state == 1:
            if state_converter[state] == "Lamborghini":
                lam_menu(lam_state, lam_previous_state)
                lam_previous_state = lam_state
                if keyboard.is_pressed("up"):
                    time.sleep(0.2)
                    lam_state = (lam_state - 1) % 5
                elif keyboard.is_pressed("down"):
                    time.sleep(0.2)
                    lam_state = (lam_state + 1) % 5
                elif keyboard.is_pressed("escape"):
                    change_in_state = 0
                    lam_state = 0
                    lam_previous_state = -1                    
            elif state_converter[state] == "Ferrari":
                fer_menu(fer_state, fer_previous_state)
                fer_previous_state = fer_state
                if keyboard.is_pressed("up"):
                    time.sleep(0.2)
                    fer_state = (fer_state - 1) % 5
                elif keyboard.is_pressed("down"):
                    time.sleep(0.2)
                    fer_state = (fer_state + 1) % 5
                elif keyboard.is_pressed("escape"):
                    change_in_state = 0
                    fer_state = 0
                    fer_previous_state = -1                    
            elif state_converter[state] == "McLaren":
                mcl_menu(mcl_state, mcl_previous_state)
                mcl_previous_state = mcl_state
                if keyboard.is_pressed("up"):
                    time.sleep(0.2)
                    mcl_state = (mcl_state - 1) % 5
                elif keyboard.is_pressed("down"):
                    time.sleep(0.2)
                    mcl_state = (mcl_state + 1) % 5
                elif keyboard.is_pressed("escape"):
                    change_in_state = 0
                    mcl_state = 0
                    mcl_previous_state = -1
if __name__ == "__main__":
    main()