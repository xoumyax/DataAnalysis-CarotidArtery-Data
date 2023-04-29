image=imread('File Location'); 
image_gray=rgb2gray(image); 
image_resize=imresize(image_gray, [270 480]); 
image_resize=im2double(image_resize);  
    figure(1); 
    imshow(image_resize); 
    title('Input Image'); 
    gamma=0.3;  
    psi=0; 
    theta=90;  
    bw=2.8;  
    lambda=3.5; 
    pi=180; 
    
    for x=1:270 
        for y=1:480
            
            x_theta=image_resize(x,y)*cos(theta)+image_resize(x,y)*sin(theta); 
            y_theta=image_resize(x,y)*sin(theta)+image_resize(x,y)*cos(theta); 
            
            gb(x,y)=exp(-(x_theta.^2/2*bw^2+ gamma^2*y_theta.^2/2*bw^2))*cos(2*pi/lambda*x_theta+psi); 
        end
    end
    
    figure(2); 
    imshow(gb); 
    title('filtered image');
    imwrite(gb,'File name');
