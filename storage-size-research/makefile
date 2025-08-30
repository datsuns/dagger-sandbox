default:

hello:
	dagger -v -i -c "hello ."

none:
	dagger -v -i -c "none"

wget:
	dagger -v -i -c "wget | terminal --cmd bash"

shell:
	dagger -v -i -c "shell . | terminal --cmd bash"

huge:
	dagger -v -i -c "mount-huge ./ | terminal --cmd bash"

clear:
	docker system prune -a --volumes

purge:
	docker builder prune

df:
	docker system df | tee -a df.txt

df_loop:
	while true; do \
		docker system df; \
		sleep 2; \
		done

vol:
	docker volume ls

inspect:
	docker volume inspect <ID>


.PNOHY: default hello purge df vol inspect
